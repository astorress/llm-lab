"""Entrena el tokenizador byte-level BPE del perfil sobre una muestra de la mezcla.

La muestra respeta la proporción de cada fuente en el corpus (tokens · repeat,
con repeat acotado a 2 para que el corpus personal no domine el vocabulario).
Así el vocabulario refleja el español técnico, el inglés, las ecuaciones y el
código en la misma proporción en que el modelo los verá.

    python scripts/train_tokenizer.py --profile small
"""

from __future__ import annotations

import argparse
import gzip
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from llm_lab.pipeline import ProfilePaths, load_profile  # noqa: E402
from llm_lab.tokenization.hf_tokenizer import train_bpe_tokenizer  # noqa: E402

MAX_DOC_CHARS = 20_000  # recorta documentos largos: acota la RAM del entrenamiento BPE


def sample_corpus(pretrain_dir: Path, n_docs: int):
    manifest = json.loads((pretrain_dir / "manifest.json").read_text())
    weights = {s: m["approx_tokens"] * min(m["repeat"], 2) for s, m in manifest.items()}
    total = sum(weights.values())
    for src, w in weights.items():
        quota = max(100, int(n_docs * w / total))
        avg_doc = manifest[src]["approx_tokens"] / max(manifest[src]["docs"], 1)
        # Fuentes de docs cortos (arXiv) necesitan más docs para el mismo peso.
        quota = int(quota * max(1.0, 1000 / max(avg_doc, 1)) ** 0.5)
        print(f"   {src:15s} → {min(quota, manifest[src]['docs']):,} docs")
        with gzip.open(pretrain_dir / f"{src}.jsonl.gz", "rt", encoding="utf-8") as f:
            for i, line in enumerate(f):
                if i >= quota:
                    break
                yield json.loads(line)["text"][:MAX_DOC_CHARS]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", default="tiny")
    args = ap.parse_args()

    cfg = load_profile(args.profile)
    paths = ProfilePaths.for_profile(args.profile)
    vocab = cfg["tokenizer"]["vocab_size"]
    print(f"🔤 Entrenando BPE byte-level · vocab {vocab:,} · perfil {args.profile}")
    tok = train_bpe_tokenizer(
        sample_corpus(paths.pretrain, cfg["tokenizer"]["sample_docs"]),
        vocab_size=vocab,
        save_path=paths.tokenizer,
    )
    for probe in ["El recocido simulado acepta soluciones peores con probabilidad exp(−Δ/T).",
                  "Kant y el imperativo categórico; la cadencia V–I en la armonía tonal",
                  "def forward(self, x: torch.Tensor) -> torch.Tensor:"]:
        enc = tok.encode(probe)
        print(f"   {len(enc.ids):3d} tokens | {' · '.join(enc.tokens[:14])}")
    print(f"→ {paths.tokenizer}")


if __name__ == "__main__":
    main()
