"""Construcción de corpus (Fase 3): limpieza, dedup, chunking, schema y balanceo."""

from llm_lab.data.chunking import (
    approx_token_count,
    chunk_fixed,
    chunk_semantic,
    chunk_sentences,
    split_sentences,
)
from llm_lab.data.cleaning import (
    QualityConfig,
    alpha_ratio,
    normalize_text,
    quality_score,
    repeated_lines_ratio,
    symbol_ratio,
)
from llm_lab.data.dedup import (
    LSHIndex,
    exact_dedup,
    jaccard_estimate,
    minhash_signature,
    sha256_hash,
    shingles,
)
from llm_lab.data.schema import load_schema, make_document, validate_document
from llm_lab.data.weighting import domain_sampling_probs, load_domain_weights

__all__ = [
    # cleaning
    "normalize_text",
    "quality_score",
    "QualityConfig",
    "alpha_ratio",
    "symbol_ratio",
    "repeated_lines_ratio",
    # dedup
    "sha256_hash",
    "exact_dedup",
    "shingles",
    "minhash_signature",
    "jaccard_estimate",
    "LSHIndex",
    # chunking
    "approx_token_count",
    "split_sentences",
    "chunk_fixed",
    "chunk_sentences",
    "chunk_semantic",
    # schema
    "load_schema",
    "make_document",
    "validate_document",
    # weighting
    "load_domain_weights",
    "domain_sampling_probs",
]
