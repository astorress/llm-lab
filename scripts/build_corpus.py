#!/usr/bin/env python3
"""Construye el corpus de entrenamiento a partir de los documentos semilla.

Pipeline reproducible que ejecuta el código real de ``llm_lab.data`` (el mismo
que se enseña en el notebook 03):

    seed_documents.SEED
        -> escribir Markdown crudo en datasets/raw/seed/
        -> normalizar + puntuar calidad
        -> dedup exacta (sha256) + near-dup (MinHash)
        -> chunking de documentos largos
        -> make_document (esquema canónico, id determinista)
        -> validar contra datasets/schemas/document.schema.json
        -> escribir datasets/processed/corpus.{jsonl,parquet}
        -> splits estratificados por dominio en datasets/splits/

Uso:
    python scripts/build_corpus.py
    python scripts/build_corpus.py --alpha 0.7 --val 0.1 --test 0.1 --seed 42
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "scripts"))

from seed_documents import SEED  # noqa: E402

from llm_lab.data.chunking import approx_token_count, chunk_fixed  # noqa: E402
from llm_lab.data.cleaning import normalize_text, quality_score  # noqa: E402
from llm_lab.data.dedup import jaccard_estimate, minhash_signature, shingles  # noqa: E402
from llm_lab.data.schema import make_document, validate_document  # noqa: E402
from llm_lab.data.weighting import domain_sampling_probs  # noqa: E402

RAW_DIR = REPO / "datasets" / "raw" / "seed"
PROC_DIR = REPO / "datasets" / "processed"
SPLIT_DIR = REPO / "datasets" / "splits"

MAX_CHUNK_TOKENS = 220   # los documentos más largos que esto se parten
NEAR_DUP_THRESHOLD = 0.8
MIN_QUALITY = 0.5


def write_raw_markdown() -> int:
    """Escribe los documentos semilla como Markdown crudo, uno por dominio."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    n = 0
    for domain, docs in SEED.items():
        lines = [f"# Corpus semilla — dominio: {domain}\n"]
        for title, subcat, diff, lang, content in docs:
            lines.append(f"\n## {title}\n")
            lines.append(f"<!-- subcategoria: {subcat} | dificultad: {diff} | idioma: {lang} -->\n")
            lines.append(content + "\n")
            n += 1
        (RAW_DIR / f"{domain}.md").write_text("".join(lines), encoding="utf-8")
    return n


def build_documents() -> list[dict]:
    """Aplica limpieza, calidad, dedup, chunking y construye documentos del esquema."""
    raw_records = []
    for domain, docs in SEED.items():
        for title, subcat, diff, lang, content in docs:
            raw_records.append(dict(domain=domain, title=title, subcategory=subcat,
                                    difficulty=diff, lang=lang, content=content))

    # --- Dedup exacta por contenido normalizado ---
    seen_hashes = set()
    deduped = []
    for r in raw_records:
        h = normalize_text(r["content"])
        if h in seen_hashes:
            continue
        seen_hashes.add(h)
        deduped.append(r)
    n_exact = len(raw_records) - len(deduped)

    # --- Dedup near-duplicate con MinHash (pairwise; corpus pequeño) ---
    sigs = [minhash_signature(shingles(r["content"], n=3), num_perm=64) for r in deduped]
    keep = [True] * len(deduped)
    n_near = 0
    for i in range(len(deduped)):
        if not keep[i]:
            continue
        for j in range(i + 1, len(deduped)):
            if keep[j] and jaccard_estimate(sigs[i], sigs[j]) > NEAR_DUP_THRESHOLD:
                keep[j] = False
                n_near += 1
    deduped = [r for r, k in zip(deduped, keep) if k]

    # --- Chunking de documentos largos + construcción del esquema ---
    documents = []
    n_filtered = 0
    for r in deduped:
        text = r["content"]
        if approx_token_count(text) > MAX_CHUNK_TOKENS:
            chunks = chunk_fixed(text, max_tokens=MAX_CHUNK_TOKENS, overlap_tokens=20)
        else:
            chunks = [text]
        total = len(chunks)
        for ci, chunk in enumerate(chunks):
            score = quality_score(chunk)
            if score < MIN_QUALITY:
                n_filtered += 1
                continue
            meta = {"language": r["lang"], "license": "CC-BY-SA-4.0 (semilla propia)",
                    "has_code": "def " in chunk or "SELECT" in chunk,
                    "has_math": any(s in chunk for s in ["=", "Σ", "∇", "δ", "²"]),
                    "extraction_method": "seed_markdown"}
            if total > 1:
                meta.update(chunk_index=ci, chunk_total=total)
            doc = make_document(
                chunk, r["domain"], source="sintetico",
                title=r["title"], subcategory=r["subcategory"], difficulty=r["difficulty"],
                metadata=meta,
            )
            documents.append(doc)

    print(f"  dedup exacta: -{n_exact}  |  near-dup: -{n_near}  |  filtrados por calidad: -{n_filtered}")
    return documents


def stratified_split(docs: list[dict], val: float, test: float, rng: random.Random):
    """Particiona estratificando por dominio (cada dominio respeta las proporciones)."""
    by_dom = defaultdict(list)
    for d in docs:
        by_dom[d["domain"]].append(d)
    train, valset, testset = [], [], []
    for dom, items in by_dom.items():
        rng.shuffle(items)
        n = len(items)
        n_test = max(1, int(round(n * test))) if n >= 3 else 0
        n_val = max(1, int(round(n * val))) if n >= 4 else 0
        testset += items[:n_test]
        valset += items[n_test:n_test + n_val]
        train += items[n_test + n_val:]
    return train, valset, testset


def write_jsonl(path: Path, docs: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for d in docs:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser(description="Construye el corpus semilla del LLM Lab")
    ap.add_argument("--alpha", type=float, default=0.7, help="exponente de weighting de dominios")
    ap.add_argument("--val", type=float, default=0.1, help="proporción de validación")
    ap.add_argument("--test", type=float, default=0.1, help="proporción de test")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    rng = random.Random(args.seed)

    print("LLM Lab — construcción del corpus semilla")
    print("=" * 60)

    n_raw = write_raw_markdown()
    print(f"1) Markdown crudo escrito: {n_raw} documentos en {RAW_DIR.relative_to(REPO)}/")

    docs = build_documents()
    print(f"2) Documentos procesados (post pipeline): {len(docs)}")

    # Validación de esquema sobre TODOS los documentos
    n_valid = 0
    for d in docs:
        errs = validate_document(d, raise_on_error=False)
        if not errs:
            n_valid += 1
        else:
            print(f"   ✗ documento inválido ({d['id'][:20]}): {errs[:2]}")
    print(f"3) Validación de esquema: {n_valid}/{len(docs)} válidos")

    # Estadísticas y weighting
    dom_counts = Counter(d["domain"] for d in docs)
    total_tokens = sum(d["tokens"] for d in docs)
    probs = domain_sampling_probs(dict(dom_counts), alpha=args.alpha)
    print(f"4) Tokens totales (estimados): {total_tokens:,} | dominios cubiertos: {len(dom_counts)}/26")

    # Splits estratificados
    train, val, test = stratified_split(docs, args.val, args.test, rng)
    write_jsonl(PROC_DIR / "corpus.jsonl", docs)
    write_jsonl(SPLIT_DIR / "train.jsonl", train)
    write_jsonl(SPLIT_DIR / "val.jsonl", val)
    write_jsonl(SPLIT_DIR / "test.jsonl", test)
    print(f"5) Escrito corpus.jsonl ({len(docs)}) + splits: train={len(train)} val={len(val)} test={len(test)}")

    # Parquet (opcional, si pandas/pyarrow disponibles)
    try:
        import pandas as pd
        df = pd.json_normalize(docs)
        df.to_parquet(PROC_DIR / "corpus.parquet")
        size_jsonl = (PROC_DIR / "corpus.jsonl").stat().st_size
        size_pq = (PROC_DIR / "corpus.parquet").stat().st_size
        print(f"6) Parquet escrito: {size_pq/1024:.1f} KB vs JSONL {size_jsonl/1024:.1f} KB")
    except Exception as e:  # noqa: BLE001
        print(f"6) Parquet omitido ({type(e).__name__}); instala pandas+pyarrow para generarlo")

    # Anti-fuga: ningún near-dup de test en train
    leak = 0
    train_sigs = [minhash_signature(shingles(d["content"], n=3), 64) for d in train]
    for t in test:
        ts = minhash_signature(shingles(t["content"], n=3), 64)
        if any(jaccard_estimate(ts, s) > NEAR_DUP_THRESHOLD for s in train_sigs):
            leak += 1
    print(f"7) Anti-fuga train/test: {leak} near-dups detectados (debe ser 0)")

    # Manifiesto del corpus
    manifest = {
        "n_documents": len(docs), "n_domains": len(dom_counts),
        "total_tokens_est": total_tokens,
        "splits": {"train": len(train), "val": len(val), "test": len(test)},
        "domain_counts": dict(dom_counts),
        "sampling_probs_alpha": args.alpha,
        "sampling_probs": {k: round(v, 4) for k, v in probs.items()},
        "min_quality": MIN_QUALITY, "near_dup_threshold": NEAR_DUP_THRESHOLD,
    }
    (PROC_DIR / "corpus_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"8) Manifiesto escrito en {(PROC_DIR / 'corpus_manifest.json').relative_to(REPO)}")
    print("=" * 60)
    print("✓ Corpus construido correctamente")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
