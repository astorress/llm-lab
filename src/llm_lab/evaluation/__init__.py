"""Evaluación (Fase 8): perplexity, métricas de texto y benchmark multiple-choice.

Carga PEREZOSA (PEP 562): importar el paquete no arrastra ``torch``. Así
``bleu_score``, ``rouge_l`` y el benchmark (Python puro) son usables sin
PyTorch; ``compute_perplexity`` (que sí necesita torch) lo importa al usarse.
"""

from __future__ import annotations

__all__ = [
    "compute_perplexity",
    "sliding_window_perplexity",
    "bleu_score",
    "rouge_l",
    "ngram_counts",
    "lcs_length",
    "MCQuestion",
    "MultipleChoiceBenchmark",
    "wilson_interval",
]

_LAZY = {
    "compute_perplexity": ("perplexity", "compute_perplexity"),          # torch
    "sliding_window_perplexity": ("perplexity", "sliding_window_perplexity"),  # torch
    "bleu_score": ("text_metrics", "bleu_score"),
    "rouge_l": ("text_metrics", "rouge_l"),
    "ngram_counts": ("text_metrics", "ngram_counts"),
    "lcs_length": ("text_metrics", "lcs_length"),
    "MCQuestion": ("benchmark", "MCQuestion"),
    "MultipleChoiceBenchmark": ("benchmark", "MultipleChoiceBenchmark"),
    "wilson_interval": ("benchmark", "wilson_interval"),
}


def __getattr__(name: str):
    if name in _LAZY:
        import importlib
        mod, attr = _LAZY[name]
        return getattr(importlib.import_module(f"llm_lab.evaluation.{mod}"), attr)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(__all__)
