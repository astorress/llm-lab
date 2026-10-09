"""Embeddings (Fase 4): Word2Vec desde cero, similitud y proyecciones.

Carga PEREZOSA (PEP 562): importar el paquete no arrastra ``torch``. Así
``cosine_similarity_matrix``, ``nearest_neighbors``, ``analogy`` y las
proyecciones (NumPy/sklearn) son usables sin PyTorch; ``SkipGramModel`` (que
necesita torch) lo importa al usarse.
"""

from __future__ import annotations

__all__ = [
    "SkipGramModel",
    "build_vocab",
    "build_training_pairs",
    "negative_sampling_table",
    "cosine_similarity_matrix",
    "nearest_neighbors",
    "analogy",
    "pca_project",
    "tsne_project",
    "umap_project",
]

_LAZY = {
    "SkipGramModel": ("word2vec", "SkipGramModel"),                  # torch
    "build_vocab": ("word2vec", "build_vocab"),
    "build_training_pairs": ("word2vec", "build_training_pairs"),
    "negative_sampling_table": ("word2vec", "negative_sampling_table"),
    "cosine_similarity_matrix": ("similarity", "cosine_similarity_matrix"),
    "nearest_neighbors": ("similarity", "nearest_neighbors"),
    "analogy": ("similarity", "analogy"),
    "pca_project": ("projections", "pca_project"),
    "tsne_project": ("projections", "tsne_project"),
    "umap_project": ("projections", "umap_project"),
}


def __getattr__(name: str):
    if name in _LAZY:
        import importlib
        mod, attr = _LAZY[name]
        return getattr(importlib.import_module(f"llm_lab.embeddings.{mod}"), attr)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(__all__)
