"""Visualización de mapas de atención (transversal, usada en Fases 5–6).

Convierte los pesos de atención (B, h, T, T) en heatmaps interpretables: qué
posiciones (columnas) atiende cada posición consulta (filas). En un decoder
causal el triángulo superior es siempre cero.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

__all__ = ["plot_attention_map", "plot_attention_heads"]


def plot_attention_map(weights, tokens=None, ax=None, title="Atención", cmap="viridis"):
    """weights: matriz (T, T) de una cabeza. tokens: etiquetas opcionales de ejes."""
    if hasattr(weights, "detach"):
        weights = weights.detach().cpu().numpy()
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(weights, cmap=cmap, aspect="auto")
    ax.set_title(title)
    ax.set_xlabel("posición atendida (key)")
    ax.set_ylabel("posición consulta (query)")
    if tokens is not None:
        ax.set_xticks(range(len(tokens)))
        ax.set_yticks(range(len(tokens)))
        ax.set_xticklabels(tokens, rotation=90, fontsize=7)
        ax.set_yticklabels(tokens, fontsize=7)
    ax.figure.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    return ax.figure


def plot_attention_heads(weights, tokens=None, max_heads=8, cmap="viridis"):
    """weights: (h, T, T) o (B, h, T, T) (toma el primer batch). Grid de cabezas."""
    if hasattr(weights, "detach"):
        weights = weights.detach().cpu().numpy()
    if weights.ndim == 4:
        weights = weights[0]
    n_heads = min(weights.shape[0], max_heads)
    cols = min(4, n_heads)
    rows = (n_heads + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(4 * cols, 3.5 * rows), squeeze=False)
    for i in range(rows * cols):
        ax = axes[i // cols][i % cols]
        if i < n_heads:
            plot_attention_map(weights[i], tokens=tokens, ax=ax, title=f"Cabeza {i}", cmap=cmap)
        else:
            ax.axis("off")
    fig.tight_layout()
    return fig
