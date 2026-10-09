"""Visualización de espacios de embeddings (transversal, usada en Fase 4)."""

from __future__ import annotations

import matplotlib.pyplot as plt

__all__ = ["plot_embeddings_2d", "plot_embeddings_3d_plotly"]


def plot_embeddings_2d(coords, labels=None, categories=None, ax=None, title="Embeddings 2D"):
    """coords: (N, 2). labels: textos por punto. categories: para colorear por grupo."""
    if hasattr(coords, "detach"):
        coords = coords.detach().cpu().numpy()
    if ax is None:
        _, ax = plt.subplots(figsize=(9, 7))

    if categories is not None:
        cats = list(dict.fromkeys(categories))
        cmap = plt.get_cmap("tab20")
        for i, cat in enumerate(cats):
            idx = [j for j, c in enumerate(categories) if c == cat]
            ax.scatter(coords[idx, 0], coords[idx, 1], s=30, color=cmap(i % 20), label=str(cat))
        ax.legend(fontsize=7, markerscale=1.2, bbox_to_anchor=(1.02, 1), loc="upper left")
    else:
        ax.scatter(coords[:, 0], coords[:, 1], s=30)

    if labels is not None:
        for j, txt in enumerate(labels):
            ax.annotate(txt, (coords[j, 0], coords[j, 1]), fontsize=7, alpha=0.8)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    return ax.figure


def plot_embeddings_3d_plotly(coords, labels=None, categories=None, title="Embeddings 3D"):
    """Proyección 3D interactiva con plotly (import perezoso). coords: (N, 3)."""
    import plotly.express as px

    if hasattr(coords, "detach"):
        coords = coords.detach().cpu().numpy()
    fig = px.scatter_3d(
        x=coords[:, 0], y=coords[:, 1], z=coords[:, 2],
        text=labels, color=categories, title=title,
    )
    fig.update_traces(marker=dict(size=4))
    return fig
