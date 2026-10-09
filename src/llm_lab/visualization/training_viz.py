"""Visualización del entrenamiento (transversal, usada en Fase 6).

Curvas de aprendizaje desde el JSONL del MetricsLogger, flujo de gradientes por
capa (diagnóstico de vanishing/exploding), histogramas de pesos y schedules de LR.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

__all__ = [
    "plot_learning_curves",
    "plot_gradient_flow",
    "plot_weight_histograms",
    "plot_lr_schedule",
]


def plot_learning_curves(history, x="step", ys=("loss", "val_loss"), ax=None):
    """history: lista de dicts o DataFrame (p.ej. MetricsLogger.to_dataframe()).

    Grafica las series ``ys`` disponibles contra ``x``.
    """
    import pandas as pd

    df = history if isinstance(history, pd.DataFrame) else pd.DataFrame(history)
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 5))
    for y in ys:
        if y in df.columns:
            sub = df.dropna(subset=[y])
            ax.plot(sub[x], sub[y], marker=".", label=y)
    ax.set_xlabel(x)
    ax.set_ylabel("valor")
    ax.set_title("Curvas de aprendizaje")
    ax.legend()
    ax.grid(True, alpha=0.3)
    return ax.figure


def plot_gradient_flow(model, ax=None):
    """Norma L2 del gradiente por parámetro con grad (llamar tras backward()).

    Barras muy bajas en capas tempranas ⇒ vanishing; picos ⇒ exploding.
    """
    names, norms = [], []
    for name, p in model.named_parameters():
        if p.requires_grad and p.grad is not None:
            names.append(name.replace("weight", "w").replace("bias", "b"))
            norms.append(p.grad.detach().norm().item())
    if ax is None:
        _, ax = plt.subplots(figsize=(10, 5))
    ax.bar(range(len(norms)), norms)
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=90, fontsize=6)
    ax.set_ylabel("‖grad‖₂")
    ax.set_title("Flujo de gradientes por capa")
    ax.grid(True, axis="y", alpha=0.3)
    return ax.figure


def plot_weight_histograms(model, max_layers=6, bins=50):
    """Histogramas de la distribución de pesos de las primeras capas Linear/Embedding."""
    params = [(n, p) for n, p in model.named_parameters() if p.dim() >= 2][:max_layers]
    cols = min(3, len(params))
    rows = (len(params) + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 3.5 * rows), squeeze=False)
    for i, (name, p) in enumerate(params):
        ax = axes[i // cols][i % cols]
        ax.hist(p.detach().cpu().numpy().ravel(), bins=bins)
        ax.set_title(name, fontsize=8)
        ax.grid(True, alpha=0.3)
    for j in range(len(params), rows * cols):
        axes[j // cols][j % cols].axis("off")
    fig.tight_layout()
    return fig


def plot_lr_schedule(lrs, ax=None):
    """lrs: lista/array de learning rates por step."""
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 4))
    ax.plot(lrs)
    ax.set_xlabel("step")
    ax.set_ylabel("learning rate")
    ax.set_title("Schedule de learning rate")
    ax.grid(True, alpha=0.3)
    return ax.figure
