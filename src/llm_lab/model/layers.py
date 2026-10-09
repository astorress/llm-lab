"""Bloques constitutivos del transformer: normalización, FFN y el bloque completo (Fase 5)."""

from __future__ import annotations

import torch
import torch.nn.functional as F
from torch import nn

from llm_lab.model.attention import MultiHeadAttention

__all__ = ["RMSNorm", "FeedForward", "TransformerBlock"]


class RMSNorm(nn.Module):
    """Root Mean Square Layer Normalization (Zhang & Sennrich, 2019).

    A diferencia de LayerNorm, NO resta la media ni usa bias: solo reescala
    por la raíz del promedio de cuadrados. Más barato y empíricamente igual de
    estable; usado en Llama, Qwen, Mistral.

        y = x / sqrt(mean(x²) + eps) * gamma
    """

    def __init__(self, d_model: int, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(d_model))  # gamma

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Cálculo en fp32 por estabilidad aunque x venga en fp16/bf16.
        norm = x.float() * torch.rsqrt(x.float().pow(2).mean(-1, keepdim=True) + self.eps)
        return (norm.type_as(x)) * self.weight


class FeedForward(nn.Module):
    """Red feed-forward por posición (la "FFN" del transformer).

    Dos variantes:
    - GELU clásica: Linear -> GELU -> Linear (GPT-2). Expansión 4×.
    - SwiGLU (Shazeer 2020, usada en Llama): rama con gate SiLU. Con SwiGLU se
      usan 3 matrices, por lo que d_ff se ajusta a ~2/3 para igualar parámetros.
    """

    def __init__(self, d_model: int, d_ff: int, dropout: float = 0.0, swiglu: bool = False):
        super().__init__()
        self.swiglu = swiglu
        if swiglu:
            self.w_gate = nn.Linear(d_model, d_ff, bias=False)
            self.w_up = nn.Linear(d_model, d_ff, bias=False)
            self.w_down = nn.Linear(d_ff, d_model, bias=False)
        else:
            self.w_up = nn.Linear(d_model, d_ff, bias=False)
            self.w_down = nn.Linear(d_ff, d_model, bias=False)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:  # (B,T,C) -> (B,T,C)
        if self.swiglu:
            # SiLU(gate) ⊙ up : el "gate" decide cuánta señal pasa por dimensión.
            h = F.silu(self.w_gate(x)) * self.w_up(x)
        else:
            h = F.gelu(self.w_up(x))
        return self.dropout(self.w_down(h))


class TransformerBlock(nn.Module):
    """Bloque transformer pre-LN (decoder-only).

    Pre-LN (normalizar ANTES de cada sub-capa) en vez de post-LN: las conexiones
    residuales quedan limpias (x + sublayer(norm(x))), lo que crea un "gradient
    highway" y permite entrenar modelos profundos sin warmup agresivo.

        x = x + Attn(norm1(x))
        x = x + FFN(norm2(x))
    """

    def __init__(
        self,
        d_model: int,
        n_heads: int,
        d_ff: int,
        n_kv_heads: int | None = None,
        dropout: float = 0.0,
        use_rope: bool = True,
        use_sdpa: bool = False,
        swiglu: bool = False,
        max_seq_len: int = 4096,
    ):
        super().__init__()
        self.norm1 = RMSNorm(d_model)
        self.attn = MultiHeadAttention(
            d_model, n_heads, n_kv_heads=n_kv_heads, dropout=dropout,
            use_rope=use_rope, use_sdpa=use_sdpa, max_seq_len=max_seq_len,
        )
        self.norm2 = RMSNorm(d_model)
        self.ffn = FeedForward(d_model, d_ff, dropout=dropout, swiglu=swiglu)

    def forward(self, x: torch.Tensor, kv_cache: dict | None = None) -> torch.Tensor:
        x = x + self.attn(self.norm1(x), kv_cache=kv_cache)
        x = x + self.ffn(self.norm2(x))
        return x
