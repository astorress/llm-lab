"""Learning rate schedulers (Fase 6).

Warmup lineal + cosine decay: el schedule estándar de los LLM modernos.

- Warmup: al inicio, los momentos de Adam están mal estimados y los pesos son
  aleatorios; un LR alto desestabiliza. Se sube linealmente de 0 a lr_max en
  ``warmup_steps``.
- Cosine decay: luego se baja siguiendo media onda de coseno hasta lr_min, lo
  que da pasos grandes al principio (exploración) y finos al final (ajuste).
"""

from __future__ import annotations

import math

__all__ = ["warmup_cosine_lr", "WarmupCosineScheduler"]


def warmup_cosine_lr(
    step: int,
    lr_max: float,
    warmup_steps: int,
    total_steps: int,
    lr_min: float = 0.0,
) -> float:
    """Devuelve el learning rate para un ``step`` dado (función pura)."""
    if warmup_steps > 0 and step < warmup_steps:
        return lr_max * (step + 1) / warmup_steps
    if step >= total_steps:
        return lr_min
    # Progreso dentro de la fase de decay en [0, 1].
    progress = (step - warmup_steps) / max(total_steps - warmup_steps, 1)
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return lr_min + (lr_max - lr_min) * cosine


class WarmupCosineScheduler:
    """Aplica ``warmup_cosine_lr`` directamente a los param_groups de un optimizador."""

    def __init__(self, optimizer, lr_max, warmup_steps, total_steps, lr_min=0.0):
        self.optimizer = optimizer
        self.lr_max = lr_max
        self.warmup_steps = warmup_steps
        self.total_steps = total_steps
        self.lr_min = lr_min
        self.step_num = 0

    def step(self) -> float:
        lr = warmup_cosine_lr(
            self.step_num, self.lr_max, self.warmup_steps, self.total_steps, self.lr_min
        )
        for group in self.optimizer.param_groups:
            group["lr"] = lr
        self.step_num += 1
        return lr

    def state_dict(self) -> dict:
        return {"step_num": self.step_num}

    def load_state_dict(self, state: dict) -> None:
        self.step_num = state["step_num"]
