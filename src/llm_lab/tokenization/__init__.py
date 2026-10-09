"""Tokenización (Fase 2): BPE educacional, tokenizador de producción y métricas."""

from llm_lab.tokenization.bpe import BPETokenizer
from llm_lab.tokenization.metrics import (
    compression,
    fertility,
    token_entropy,
    vocab_coverage,
)

__all__ = [
    "BPETokenizer",
    "fertility",
    "compression",
    "vocab_coverage",
    "token_entropy",
    # train_bpe_tokenizer / load_tokenizer requieren `tokenizers`: import directo
    # desde llm_lab.tokenization.hf_tokenizer para no forzar la dependencia aquí.
]
