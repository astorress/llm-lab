"""Visualización transversal: atención, entrenamiento y embeddings.

Las funciones reciben un ``ax`` opcional y devuelven la figura. matplotlib y
seaborn se importan directamente; plotly de forma perezosa dentro de cada función.
"""

from llm_lab.visualization.attention_viz import plot_attention_heads, plot_attention_map
from llm_lab.visualization.embedding_viz import (
    plot_embeddings_2d,
    plot_embeddings_3d_plotly,
)
from llm_lab.visualization.training_viz import (
    plot_gradient_flow,
    plot_learning_curves,
    plot_lr_schedule,
    plot_weight_histograms,
)

__all__ = [
    "plot_attention_map",
    "plot_attention_heads",
    "plot_learning_curves",
    "plot_gradient_flow",
    "plot_weight_histograms",
    "plot_lr_schedule",
    "plot_embeddings_2d",
    "plot_embeddings_3d_plotly",
]
