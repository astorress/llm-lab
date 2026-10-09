"""Construye el corpus de PRE-ENTRENAMIENTO del perfil (Fase 3 a escala real).

Por cada fuente de ``configs/data.yaml``: descarga en streaming (HF) o lee
(local), limpia, filtra por calidad y dominio, deduplica por hash exacto y
escribe ``datasets/pretrain/<perfil>/<fuente>.jsonl.gz`` hasta llenar su
presupuesto ``share · total_tokens``. Las fuentes corren en paralelo
(un proceso por fuente) y el paso es reanudable: una fuente con ``.done``
no se vuelve a procesar.

    python scripts/build_pretrain_corpus.py --profile tiny
    python scripts/build_pretrain_corpus.py --profile small --workers 8
    python scripts/build_pretrain_corpus.py --profile small --only arxiv,cosmopedia --force

Recomendación: correr este paso en tu Mac (devcontainer, 14 CPUs, gratis) y
subir solo el resultado tokenizado a Drive/Kaggle. Ver docs/07.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import random
import sys
import time
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from llm_lab.pipeline import ProfilePaths, load_data_config  # noqa: E402


def build_source(name: str, spec: dict, budget: int | None, out_dir: str,
                 max_domain_share: float) -> dict:
    """Procesa una fuente completa. Corre en un proceso hijo."""
    from llm_lab.data.cleaning import QualityConfig
    from llm_lab.data.domains import DomainClassifier
    from llm_lab.data.sources import approx_tokens, iter_source
    from llm_lab.data.weighting import load_domain_weights

    out_path = Path(out_dir) / f"{name}.jsonl.gz"
    tmp_path = out_path.with_suffix(".tmp")
    classifier = DomainClassifier()
    seen: set[bytes] = set()
    tokens, docs, scanned = 0, 0, 0
    per_domain: Counter = Counter()
    # Tope por dominio solo en fuentes mixtas con presupuesto (no en las de
    # dominio fijo como open_web_math → matemáticas o code_python → python).
    cap = max_domain_share * budget if budget and not spec.get("default_domain") else None
    # Pesos de configs/corpus.yaml: en fuentes mixtas con presupuesto, un doc del
    # dominio d se acepta con prob. w_d / max(w) → los temas prioritarios (1.5)
    # ocupan más presupuesto que el resto (1.0 → 67 % de aceptación).
    weights = load_domain_weights()
    w_max = max(weights.values())
    rng = random.Random(f"{name}-seed")
    t0 = time.time()

    with gzip.open(tmp_path, "wt", encoding="utf-8") as f:
        for doc in iter_source(name, spec, ROOT, classifier, QualityConfig()):
            scanned += 1
            h = hashlib.sha1(doc["text"].encode()).digest()
            if h in seen:
                continue
            n = approx_tokens(doc["text"])
            if cap and per_domain[doc["domain"]] + n > cap:
                continue
            if cap and rng.random() > weights.get(doc["domain"], 1.0) / w_max:
                continue
            seen.add(h)
            f.write(json.dumps(doc, ensure_ascii=False) + "\n")
            tokens += n
            docs += 1
            per_domain[doc["domain"]] += n
            if docs % 20000 == 0:
                rate = tokens / (time.time() - t0)
                print(f"   [{name}] {tokens / 1e6:7.1f} M tok / "
                      f"{(budget or 0) / 1e6:.0f} M · {rate / 1e3:.0f} k tok/s", flush=True)
            if budget and tokens >= budget:
                break

    tmp_path.rename(out_path)
    stats = {"source": name, "docs": docs, "approx_tokens": tokens, "scanned": scanned,
             "budget": budget, "repeat": spec.get("repeat", 1), "lang": spec.get("lang"),
             "domains": dict(per_domain.most_common()), "seconds": round(time.time() - t0)}
    (Path(out_dir) / f"{name}.done").write_text(json.dumps(stats, ensure_ascii=False, indent=2))
    return stats


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--profile", default="tiny")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--only", default="", help="lista de fuentes separadas por coma")
    ap.add_argument("--force", action="store_true", help="reprocesa aunque exista .done")
    args = ap.parse_args()

    cfg, sources = load_data_config(args.profile)
    if args.only:
        sources = {k: v for k, v in sources.items() if k in args.only.split(",")}
    paths = ProfilePaths.for_profile(args.profile)
    paths.pretrain.mkdir(parents=True, exist_ok=True)
    total = cfg["total_tokens"]

    jobs = {}
    for name, spec in sources.items():
        done = paths.pretrain / f"{name}.done"
        if done.exists() and not args.force:
            print(f"↷ {name}: ya construido (usa --force para rehacer)")
            continue
        budget = int(spec["share"] * total) if spec["type"] == "hf" else None
        jobs[name] = (spec, budget)

    print(f"📚 Perfil {args.profile} · presupuesto total {total / 1e6:.0f} M tokens · "
          f"{len(jobs)} fuentes por procesar")
    with ProcessPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {pool.submit(build_source, n, s, b, str(paths.pretrain), cfg["max_domain_share"]): n
                   for n, (s, b) in jobs.items()}
        for fut in as_completed(futures):
            name = futures[fut]
            try:
                st = fut.result()
                print(f"✓ {name}: {st['docs']:,} docs · {st['approx_tokens'] / 1e6:.1f} M tok "
                      f"({st['scanned']:,} leídos, {st['seconds']} s)")
            except Exception as exc:
                print(f"✗ {name}: {exc.__class__.__name__}: {exc}")

    manifest = {p.stem: json.loads(p.read_text()) for p in sorted(paths.pretrain.glob("*.done"))}
    (paths.pretrain / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    eff = sum(m["approx_tokens"] * m["repeat"] for m in manifest.values())
    print(f"\n📦 {len(manifest)} fuentes · ~{eff / 1e6:.1f} M tokens efectivos (con repeticiones)"
          f"\n→ {paths.pretrain / 'manifest.json'}")


if __name__ == "__main__":
    main()
