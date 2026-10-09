"""Tokeniza el corpus de pre-entrenamiento a archivos binarios (memmap).

Para cada fuente escribe ``train_<fuente>.bin`` (doc <eot> doc <eot> ...) y
separa ~``val_fraction`` de los documentos (por hash, determinista) hacia
``val.bin``. Los documentos de validación del corpus personal se copian
además a ``val_personal.bin``: es la métrica que dice cuánto aprendió de TI.

    python scripts/tokenize_corpus.py --profile small

Tamaño en disco: 2 bytes/token (uint16, vocab < 65 536) → 350 M tokens ≈ 700 MB.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from llm_lab.pipeline import ProfilePaths, load_data_config  # noqa: E402
from llm_lab.tokenization.hf_tokenizer import load_tokenizer  # noqa: E402

BATCH = 2000


def is_val(text: str, fraction: float) -> bool:
    return int(hashlib.md5(text.encode()).hexdigest()[:8], 16) % 100_000 < fraction * 100_000


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", default="tiny")
    args = ap.parse_args()

    data_cfg, _ = load_data_config(args.profile)
    paths = ProfilePaths.for_profile(args.profile)
    paths.tokenized.mkdir(parents=True, exist_ok=True)
    tok = load_tokenizer(paths.tokenizer)
    vocab = tok.get_vocab_size()
    eot = tok.token_to_id("<|endoftext|>")
    dtype = np.uint16 if vocab < 2**16 else np.uint32
    manifest = json.loads((paths.pretrain / "manifest.json").read_text())

    val_f = open(paths.tokenized / "val.bin", "wb")
    valp_f = open(paths.tokenized / "val_personal.bin", "wb")
    meta = {"vocab_size": vocab, "dtype": np.dtype(dtype).name, "eot_id": eot,
            "tokenizer": str(paths.tokenizer), "sources": {}, "domains": {}}
    domains: Counter = Counter()
    val_total = valp_total = 0

    for src, info in manifest.items():
        train_tokens = val_tokens = 0
        with gzip.open(paths.pretrain / f"{src}.jsonl.gz", "rt", encoding="utf-8") as fin, \
                open(paths.tokenized / f"train_{src}.bin", "wb") as ftrain:
            batch: list[dict] = []

            def flush() -> None:
                nonlocal train_tokens, val_tokens, val_total, valp_total
                encs = tok.encode_batch([d["text"] for d in batch], add_special_tokens=False)
                for d, e in zip(batch, encs):
                    ids = np.array(e.ids + [eot], dtype=dtype)
                    if is_val(d["text"], data_cfg["val_fraction"]):
                        ids.tofile(val_f)
                        val_tokens += len(ids)
                        val_total += len(ids)
                        if src == "personal":
                            ids.tofile(valp_f)
                            valp_total += len(ids)
                    else:
                        ids.tofile(ftrain)
                        train_tokens += len(ids)
                        domains[d["domain"]] += len(ids) * info["repeat"]
                batch.clear()

            for line in fin:
                batch.append(json.loads(line))
                if len(batch) >= BATCH:
                    flush()
            if batch:
                flush()

        meta["sources"][src] = {"train_tokens": train_tokens, "val_tokens": val_tokens,
                                "repeat": info["repeat"], "docs": info["docs"], "lang": info["lang"]}
        print(f"✓ {src:15s} {train_tokens / 1e6:8.2f} M train · {val_tokens / 1e3:7.1f} k val "
              f"· ×{info['repeat']}")

    val_f.close()
    valp_f.close()
    eff = sum(s["train_tokens"] * s["repeat"] for s in meta["sources"].values())
    meta["domains"] = {d: round(n / eff, 4) for d, n in domains.most_common()}
    meta["effective_train_tokens"] = eff
    meta["val_tokens"] = val_total
    meta["val_personal_tokens"] = valp_total
    (paths.tokenized / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2))

    print(f"\n📦 {eff / 1e6:.1f} M tokens efectivos · val {val_total / 1e3:.0f} k "
          f"(personal {valp_total / 1e3:.0f} k) · dtype {meta['dtype']}")
    print("   mezcla por dominio:", {k: f"{v:.1%}" for k, v in list(meta["domains"].items())[:8]}, "…")
    print(f"→ {paths.tokenized}")


if __name__ == "__main__":
    main()
