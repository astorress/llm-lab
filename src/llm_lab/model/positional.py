"""Codificaciones posicionales (Fase 5).

La atención es permutation-invariant: sin información de posición, "el voltaje
sube" y "sube el voltaje" producen el mismo conjunto de salidas. Hay que
inyectar el orden. Dos enfoques implementados aquí:

- Sinusoidal absoluta (Vaswani et al., 2017): suma vectores fijos a los
  embeddings.
- RoPE (Su et al., 2021): rota los vectores Q y K por un ángulo proporcional
  a la posición. Su gracia: el producto punto q_m·k_n termina dependiendo solo
  de la posición RELATIVA (m - n), no de las absolutas. Es el estándar moderno
  (Llama, Qwen, Mistral).
"""

from __future__ import annotations

import math

import torch

__all__ = ["sinusoidal_encoding", "RotaryEmbedding"]


def sinusoidal_encoding(seq_len: int, d_model: int, device=None) -> torch.Tensor:
    """Matriz de codificación posicional sinusoidal de shape (seq_len, d_model).

    PE[pos, 2i]   = sin(pos / 10000^(2i/d))
    PE[pos, 2i+1] = cos(pos / 10000^(2i/d))

    La elección sin/cos permite expresar PE[pos+k] como combinación lineal de
    PE[pos] (rotación), lo que da al modelo una forma fácil de atender a
    desplazamientos relativos fijos.
    """
    pe = torch.zeros(seq_len, d_model, device=device)  # (T, d)
    position = torch.arange(seq_len, device=device).unsqueeze(1).float()  # (T, 1)
    # div_term = 1 / 10000^(2i/d) calculado en log-espacio por estabilidad.
    div_term = torch.exp(
        torch.arange(0, d_model, 2, device=device).float()
        * (-math.log(10000.0) / d_model)
    )  # (d/2,)
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    return pe  # (T, d)


class RotaryEmbedding(torch.nn.Module):
    """Rotary Positional Embeddings (RoPE).

    Trata cada par de dimensiones (2i, 2i+1) de Q/K como un número complejo y
    lo rota un ángulo pos·θ_i, con θ_i = base^(-2i/d). Como una rotación de m
    seguida de la inversa de n equivale a una rotación de (m-n), el producto
    punto entre query en posición m y key en posición n solo depende de m-n:
    RoPE codifica posición relativa sin tablas aprendidas ni términos extra.
    """

    def __init__(self, head_dim: int, base: float = 10000.0, max_seq_len: int = 4096):
        super().__init__()
        if head_dim % 2 != 0:
            raise ValueError("head_dim debe ser par para RoPE")
        self.head_dim = head_dim
        self.base = base
        # inv_freq: frecuencias θ_i para cada par de dimensiones. (head_dim/2,)
        inv_freq = 1.0 / (base ** (torch.arange(0, head_dim, 2).float() / head_dim))
        self.register_buffer("inv_freq", inv_freq, persistent=False)
        self._build_cache(max_seq_len)

    def _build_cache(self, seq_len: int) -> None:
        """Precalcula cos/sen para todas las posiciones hasta seq_len."""
        t = torch.arange(seq_len).float()  # (T,)
        freqs = torch.outer(t, self.inv_freq)  # (T, head_dim/2)
        # Se duplica para cubrir las dos mitades del vector. (T, head_dim)
        emb = torch.cat([freqs, freqs], dim=-1)
        self.register_buffer("_cos", emb.cos(), persistent=False)
        self.register_buffer("_sin", emb.sin(), persistent=False)
        self._cached_len = seq_len

    @staticmethod
    def _rotate_half(x: torch.Tensor) -> torch.Tensor:
        """Rota las dos mitades: [x1, x2] -> [-x2, x1]. (la parte imaginaria)."""
        half = x.shape[-1] // 2
        x1, x2 = x[..., :half], x[..., half:]
        return torch.cat([-x2, x1], dim=-1)

    def forward(self, q: torch.Tensor, k: torch.Tensor):
        """Aplica RoPE a query y key.

        q, k: (B, n_heads, T, head_dim). Devuelve los tensores rotados con la
        misma shape.
        """
        seq_len = q.shape[-2]
        if seq_len > self._cached_len:
            self._build_cache(seq_len)
        cos = self._cos[:seq_len].to(q.dtype)  # (T, head_dim)
        sin = self._sin[:seq_len].to(q.dtype)
        # Broadcasting sobre (B, n_heads): (1, 1, T, head_dim)
        cos = cos.unsqueeze(0).unsqueeze(0)
        sin = sin.unsqueeze(0).unsqueeze(0)
        q_rot = q * cos + self._rotate_half(q) * sin
        k_rot = k * cos + self._rotate_half(k) * sin
        return q_rot, k_rot
