"""LoRA (Low-Rank Adaptation) desde cero (Fase 7).

Hu et al. (2021): en vez de actualizar W (d×k), se congela y se le suma una
actualización de bajo rango ΔW = (α/r)·B·A, con A (r×k) y B (d×r), r ≪ min(d,k).
Solo A y B se entrenan: parámetros entrenables caen de d·k a r·(d+k).

B se inicializa en cero ⇒ al empezar ΔW = 0 y el modelo es idéntico al base
(el fine-tuning arranca sin perturbar). El factor α/r desacopla la magnitud de
la adaptación del rango elegido.
"""

from __future__ import annotations

import math

import torch
from torch import nn

__all__ = [
    "LoRALinear",
    "inject_lora",
    "merge_lora",
    "mark_only_lora_trainable",
    "count_trainable",
]


class LoRALinear(nn.Module):
    """Envuelve un ``nn.Linear`` congelado y le añade la rama LoRA entrenable."""

    def __init__(self, base: nn.Linear, r: int = 8, alpha: int = 16, dropout: float = 0.0):
        super().__init__()
        self.base = base
        for p in self.base.parameters():
            p.requires_grad = False  # congelar el peso preentrenado

        self.r = r
        self.alpha = alpha
        self.scaling = alpha / r
        in_f, out_f = base.in_features, base.out_features
        # A: (r, in) inicializada con Kaiming; B: (out, r) en cero.
        self.lora_A = nn.Parameter(torch.empty(r, in_f))
        self.lora_B = nn.Parameter(torch.zeros(out_f, r))
        nn.init.kaiming_uniform_(self.lora_A, a=math.sqrt(5))
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # y = W·x  +  (α/r)·B·A·x
        base_out = self.base(x)
        lora_out = self.dropout(x) @ self.lora_A.t() @ self.lora_B.t()
        return base_out + self.scaling * lora_out

    @torch.no_grad()
    def merged_weight(self) -> torch.Tensor:
        """Devuelve W + ΔW efectivo, para fusionar en inferencia."""
        delta = self.scaling * (self.lora_B @ self.lora_A)  # (out, in)
        return self.base.weight.data + delta


def _get_module(model: nn.Module, name: str) -> nn.Module:
    parent = model
    parts = name.split(".")
    for p in parts[:-1]:
        parent = getattr(parent, p)
    return parent, parts[-1]


def inject_lora(model: nn.Module, target_substrings, r: int = 8, alpha: int = 16, dropout: float = 0.0) -> int:
    """Reemplaza por LoRALinear cada nn.Linear cuyo nombre contenga algún substring.

    target_substrings: p.ej. ["w_q", "w_v"] para adaptar solo las proyecciones
    de query y value (la elección común). Devuelve cuántas capas se inyectaron.
    """
    to_replace = []
    for name, module in model.named_modules():
        if isinstance(module, nn.Linear) and any(s in name for s in target_substrings):
            to_replace.append(name)
    for name in to_replace:
        parent, attr = _get_module(model, name)
        base = getattr(parent, attr)
        setattr(parent, attr, LoRALinear(base, r=r, alpha=alpha, dropout=dropout))
    return len(to_replace)


def merge_lora(model: nn.Module) -> int:
    """Fusiona todas las ramas LoRA en sus pesos base y las reemplaza por Linear plano."""
    merged = 0
    for name, module in list(model.named_modules()):
        if isinstance(module, LoRALinear):
            parent, attr = _get_module(model, name)
            base = module.base
            base.weight.data = module.merged_weight()
            for p in base.parameters():
                p.requires_grad = True
            setattr(parent, attr, base)
            merged += 1
    return merged


def mark_only_lora_trainable(model: nn.Module) -> None:
    """Congela todo excepto los parámetros LoRA (lora_A / lora_B)."""
    for name, p in model.named_parameters():
        p.requires_grad = "lora_" in name


def count_trainable(model: nn.Module) -> dict[str, int | float]:
    """Cuenta parámetros entrenables vs totales y el porcentaje."""
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    return {
        "trainable": trainable,
        "total": total,
        "trainable_pct": 100.0 * trainable / max(total, 1),
    }
