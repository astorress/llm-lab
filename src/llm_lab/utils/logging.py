"""Logging estructurado: consola legible + métricas en JSONL para análisis posterior.

Dos piezas:
- ``get_logger``: logger estándar de Python con formato consistente.
- ``MetricsLogger``: registra métricas por paso en un archivo .jsonl,
  de modo que las curvas de entrenamiento se puedan reconstruir con
  pandas sin depender de TensorBoard/W&B (fuera de alcance en Etapa 1).
"""

from __future__ import annotations

import json
import logging
import sys
import time
from pathlib import Path


def get_logger(name: str = "llm_lab", level: str = "INFO") -> logging.Logger:
    """Logger con formato uniforme. Idempotente (no duplica handlers)."""
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
                          datefmt="%H:%M:%S")
    )
    logger.addHandler(handler)
    logger.propagate = False
    return logger


class MetricsLogger:
    """Acumula métricas por paso y las persiste como JSON Lines.

    Cada línea es un dict: {"step": int, "wall_time": float, **metrics}.
    Reconstruir curvas: ``pd.read_json("logs/metrics_run1.jsonl", lines=True)``.
    """

    def __init__(self, run_name: str, log_dir: str | Path = "logs") -> None:
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.path = self.log_dir / f"metrics_{run_name}.jsonl"
        self._t0 = time.time()
        self.history: list[dict] = []

    def log(self, step: int, **metrics: float) -> None:
        """Registra un punto de métricas asociado a un paso de entrenamiento."""
        record = {"step": step, "wall_time": round(time.time() - self._t0, 2), **metrics}
        self.history.append(record)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

    def to_dataframe(self):
        """Devuelve el historial como DataFrame de pandas (import perezoso)."""
        import pandas as pd
        return pd.DataFrame(self.history)
