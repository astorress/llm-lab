"""Reproducibilidad: fijación de seeds en todas las fuentes de aleatoriedad.

Un experimento de ML tiene al menos CUATRO fuentes de aleatoriedad:
1. ``random`` de Python (shuffling de listas, sampling simple)
2. NumPy (inicializaciones, sampling de datasets)
3. PyTorch CPU (inicialización de pesos, dropout)
4. PyTorch CUDA (kernels no deterministas, cuDNN autotuner)

Fijar solo una de ellas NO garantiza reproducibilidad.
"""

from __future__ import annotations

import os
import random

import numpy as np
import torch


def set_seed(seed: int = 42, deterministic_cudnn: bool = True) -> int:
    """Fija la seed en Python, NumPy y PyTorch (CPU + todas las GPUs).

    Args:
        seed: valor de la seed global.
        deterministic_cudnn: si True, fuerza algoritmos deterministas en cuDNN.
            Esto puede reducir el throughput ~5-10% pero garantiza que dos
            ejecuciones con la misma seed produzcan exactamente los mismos
            tensores. Para benchmarks de velocidad usar False.

    Returns:
        La seed utilizada (útil para registrarla en logs).
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

    # PYTHONHASHSEED afecta el orden de iteración de sets/dicts entre procesos
    os.environ["PYTHONHASHSEED"] = str(seed)

    if deterministic_cudnn and torch.cuda.is_available():
        # benchmark=True deja que cuDNN elija el kernel más rápido por
        # heurística (no determinista entre ejecuciones); lo desactivamos.
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True

    return seed
