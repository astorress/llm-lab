"""Self-attention causal y Multi-Head Attention (Fase 5).

Convención de shapes en todo el módulo:
    B = batch, T = longitud de secuencia, C = d_model, h = nº de cabezas,
    d_k = C / h = dimensión por cabeza.

Incluye soporte para Grouped Query Attention (GQA): menos cabezas de K/V que
de Q, lo que reduce el tamaño del KV-cache en inferencia (MQA es el caso
extremo n_kv_heads=1).
"""

from __future__ import annotations

import math

import torch
import torch.nn.functional as F
from torch import nn

from llm_lab.model.positional import RotaryEmbedding

__all__ = ["scaled_dot_product_attention", "MultiHeadAttention"]


def scaled_dot_product_attention(
    q: torch.Tensor,
    k: torch.Tensor,
    v: torch.Tensor,
    causal: bool = True,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Attention escalada desde cero (sin usar el kernel fusionado de PyTorch).

    q, k, v: (B, h, T, d_k). Devuelve (salida (B, h, T, d_k), pesos (B, h, T, T)).

    scores = QKᵀ / √d_k. El factor 1/√d_k mantiene la varianza de los scores
    en ~1 aunque crezca d_k: sin él, los productos punto escalan con d_k, el
    softmax se satura y los gradientes se desvanecen.
    """
    d_k = q.shape[-1]
    scores = (q @ k.transpose(-2, -1)) / math.sqrt(d_k)  # (B, h, T, T)
    if causal:
        T = scores.shape[-1]
        # Máscara triangular superior: prohíbe atender a posiciones futuras.
        mask = torch.triu(torch.ones(T, T, device=scores.device, dtype=torch.bool), diagonal=1)
        scores = scores.masked_fill(mask, float("-inf"))
    weights = F.softmax(scores, dim=-1)  # (B, h, T, T)
    out = weights @ v  # (B, h, T, d_k)
    return out, weights


class MultiHeadAttention(nn.Module):
    """Multi-Head Attention con RoPE opcional, GQA y KV-cache.

    Args:
        d_model: dimensión del modelo (C).
        n_heads: nº de cabezas de query.
        n_kv_heads: nº de cabezas de key/value (None = igual a n_heads = MHA).
            n_kv_heads < n_heads activa GQA; n_kv_heads=1 es MQA.
        dropout: prob. de dropout sobre la salida.
        use_rope: aplicar RoPE a Q y K.
        use_sdpa: usar F.scaled_dot_product_attention (rápido, Flash si hay GPU)
            en lugar de la implementación didáctica. No expone los pesos.
        max_seq_len: para el cache de RoPE.
    """

    def __init__(
        self,
        d_model: int,
        n_heads: int,
        n_kv_heads: int | None = None,
        dropout: float = 0.0,
        use_rope: bool = True,
        use_sdpa: bool = False,
        max_seq_len: int = 4096,
    ):
        super().__init__()
        if d_model % n_heads != 0:
            raise ValueError("d_model debe ser divisible entre n_heads")
        self.d_model = d_model
        self.n_heads = n_heads
        self.n_kv_heads = n_kv_heads or n_heads
        if n_heads % self.n_kv_heads != 0:
            raise ValueError("n_heads debe ser múltiplo de n_kv_heads (GQA)")
        self.n_rep = n_heads // self.n_kv_heads  # cuántas Q comparten cada KV
        self.d_k = d_model // n_heads
        self.use_rope = use_rope
        self.use_sdpa = use_sdpa
        self.dropout_p = dropout

        # Proyecciones. Q tiene n_heads·d_k = d_model; K y V tienen n_kv_heads·d_k.
        self.w_q = nn.Linear(d_model, n_heads * self.d_k, bias=False)
        self.w_k = nn.Linear(d_model, self.n_kv_heads * self.d_k, bias=False)
        self.w_v = nn.Linear(d_model, self.n_kv_heads * self.d_k, bias=False)
        self.w_o = nn.Linear(d_model, d_model, bias=False)
        self.resid_dropout = nn.Dropout(dropout)

        self.rope = RotaryEmbedding(self.d_k, max_seq_len=max_seq_len) if use_rope else None
        self.last_attn_weights: torch.Tensor | None = None  # para visualización

    def _repeat_kv(self, x: torch.Tensor) -> torch.Tensor:
        """Expande las cabezas KV para casar con las Q (GQA). (B,n_kv,T,d_k)->(B,n_heads,T,d_k)."""
        if self.n_rep == 1:
            return x
        B, n_kv, T, d_k = x.shape
        return (
            x[:, :, None, :, :]
            .expand(B, n_kv, self.n_rep, T, d_k)
            .reshape(B, n_kv * self.n_rep, T, d_k)
        )

    def forward(
        self,
        x: torch.Tensor,
        kv_cache: dict | None = None,
    ) -> torch.Tensor:
        """x: (B, T, C). Devuelve (B, T, C).

        Si se pasa ``kv_cache`` (dict con claves 'k','v'), concatena los K/V
        previos — usado en generación autoregresiva para no recomputar el
        prefijo (KV-cache).
        """
        B, T, C = x.shape
        q = self.w_q(x).view(B, T, self.n_heads, self.d_k).transpose(1, 2)      # (B,h,T,d_k)
        k = self.w_k(x).view(B, T, self.n_kv_heads, self.d_k).transpose(1, 2)   # (B,n_kv,T,d_k)
        v = self.w_v(x).view(B, T, self.n_kv_heads, self.d_k).transpose(1, 2)

        if self.rope is not None:
            # RoPE espera misma d_k en q y k; rotamos por separado por nº de cabezas.
            q, _ = self.rope(q, q)
            k, _ = self.rope(k, k)

        if kv_cache is not None and "k" in kv_cache:
            k = torch.cat([kv_cache["k"], k], dim=2)
            v = torch.cat([kv_cache["v"], v], dim=2)
        if kv_cache is not None:
            kv_cache["k"], kv_cache["v"] = k, v

        k = self._repeat_kv(k)  # (B,h,T,d_k)
        v = self._repeat_kv(v)

        # Con cache, las queries nuevas (T pequeño) atienden a todo el pasado:
        # is_causal solo aplica cuando q y k tienen la misma longitud.
        causal = k.shape[2] == q.shape[2]

        if self.use_sdpa:
            out = F.scaled_dot_product_attention(
                q, k, v, is_causal=causal, dropout_p=self.dropout_p if self.training else 0.0
            )  # (B,h,T,d_k)
            self.last_attn_weights = None
        else:
            out, weights = scaled_dot_product_attention(q, k, v, causal=causal)
            self.last_attn_weights = weights.detach()

        out = out.transpose(1, 2).contiguous().view(B, T, C)  # (B,T,C)
        return self.resid_dropout(self.w_o(out))
