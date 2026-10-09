"""Checkpointing reanudable (Fase 6).

Guarda el estado COMPLETO necesario para que reanudar produzca exactamente la
misma trayectoria que un entrenamiento sin interrupción: pesos, optimizador,
scheduler, GradScaler y el estado de TODOS los generadores de aleatoriedad
(Python, NumPy, PyTorch CPU y CUDA). Ver docs/03_arquitectura.md.
"""

from __future__ import annotations

import random
from pathlib import Path

import numpy as np
import torch

__all__ = ["save_checkpoint", "load_checkpoint"]


def _rng_state() -> dict:
    """Captura el estado de las 4 fuentes de aleatoriedad."""
    state = {
        "python": random.getstate(),
        "numpy": np.random.get_state(),
        "torch": torch.get_rng_state(),
    }
    if torch.cuda.is_available():
        state["cuda"] = torch.cuda.get_rng_state_all()
    return state


def _set_rng_state(state: dict) -> None:
    random.setstate(state["python"])
    np.random.set_state(state["numpy"])
    torch.set_rng_state(state["torch"])
    if "cuda" in state and torch.cuda.is_available():
        torch.cuda.set_rng_state_all(state["cuda"])


def save_checkpoint(
    path: str | Path,
    step: int,
    model,
    optimizer,
    scheduler=None,
    scaler=None,
    config: dict | None = None,
    metrics: dict | None = None,
) -> Path:
    """Persiste un checkpoint completo en ``path``."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    ckpt = {
        "step": step,
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
        "scheduler_state_dict": scheduler.state_dict() if scheduler is not None else None,
        "scaler_state_dict": scaler.state_dict() if scaler is not None else None,
        "rng_state": _rng_state(),
        "config": config,
        "metrics": metrics or {},
    }
    torch.save(ckpt, path)
    return path


def load_checkpoint(
    path: str | Path,
    model,
    optimizer=None,
    scheduler=None,
    scaler=None,
    map_location="cpu",
    restore_rng: bool = True,
) -> dict:
    """Restaura un checkpoint. Devuelve el dict completo (para leer step/metrics)."""
    ckpt = torch.load(path, map_location=map_location, weights_only=False)
    model.load_state_dict(ckpt["model_state_dict"])
    if optimizer is not None and ckpt.get("optimizer_state_dict"):
        optimizer.load_state_dict(ckpt["optimizer_state_dict"])
    if scheduler is not None and ckpt.get("scheduler_state_dict"):
        scheduler.load_state_dict(ckpt["scheduler_state_dict"])
    if scaler is not None and ckpt.get("scaler_state_dict"):
        scaler.load_state_dict(ckpt["scaler_state_dict"])
    if restore_rng and ckpt.get("rng_state"):
        _set_rng_state(ckpt["rng_state"])
    return ckpt
