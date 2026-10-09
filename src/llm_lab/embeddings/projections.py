"""Reducción de dimensionalidad para visualizar embeddings (Fase 4).

PCA (lineal, preserva varianza global), t-SNE (no lineal, preserva vecindarios
locales) y UMAP (no lineal, mejor estructura global que t-SNE y más rápido).
Las dependencias se importan de forma perezosa; UMAP es opcional.
"""

from __future__ import annotations

import numpy as np

__all__ = ["pca_project", "tsne_project", "umap_project"]


def _to_numpy(x):
    return x.detach().cpu().numpy() if hasattr(x, "detach") else np.asarray(x)


def pca_project(vectors, n_components: int = 2):
    """PCA vía scikit-learn. Devuelve (coords, varianza_explicada)."""
    from sklearn.decomposition import PCA

    v = _to_numpy(vectors)
    pca = PCA(n_components=n_components)
    coords = pca.fit_transform(v)
    return coords, pca.explained_variance_ratio_


def tsne_project(vectors, n_components: int = 2, perplexity: float = 30.0, random_state: int = 42):
    """t-SNE vía scikit-learn. perplexity controla el tamaño del vecindario."""
    from sklearn.manifold import TSNE

    v = _to_numpy(vectors)
    # perplexity debe ser < n_samples.
    perplexity = min(perplexity, max(5, v.shape[0] - 1))
    tsne = TSNE(n_components=n_components, perplexity=perplexity,
                init="pca", random_state=random_state)
    return tsne.fit_transform(v)


def umap_project(vectors, n_components: int = 2, n_neighbors: int = 15, random_state: int = 42):
    """UMAP (opcional). Lanza ImportError claro si umap-learn no está instalado."""
    try:
        import umap
    except ImportError as e:
        raise ImportError(
            "umap-learn no está instalado. `pip install umap-learn` o usa pca_project/tsne_project."
        ) from e

    v = _to_numpy(vectors)
    n_neighbors = min(n_neighbors, max(2, v.shape[0] - 1))
    reducer = umap.UMAP(n_components=n_components, n_neighbors=n_neighbors, random_state=random_state)
    return reducer.fit_transform(v)
