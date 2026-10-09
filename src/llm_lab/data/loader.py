"""DataLoader de pre-entrenamiento sobre tokens en memmap (Fase 6).

Formato en disco (escrito por ``scripts/tokenize_corpus.py``)::

    datasets/tokenized/<perfil>/
        train_<fuente>.bin   # uint16/uint32 contiguo: doc1 <eot> doc2 <eot> ...
        val.bin              # validación general (todas las fuentes)
        val_personal.bin     # validación SOLO de tu corpus personal
        meta.json            # vocab, dtype, tokens por fuente/dominio

Muestreo de un batch (estilo nanoGPT + mezcla ponderada):

    1. fuente  s ~ Categorical(p),  p_s ∝ tokens_s · repeat_s
    2. offset  i ~ U[0, N_s − T − 1]
    3. x = tokens[i : i+T],  y = tokens[i+1 : i+T+1]

Como la ponderación vive aquí (no en disco), re-balancear la mezcla no exige
re-tokenizar. Los documentos están separados por <|endoftext|>, así que una
ventana puede cruzar documentos: el modelo aprende a "reiniciar" tras el eot
(document packing, igual que GPT-2/3).
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import torch

__all__ = ["TokenDataset"]


class TokenDataset:
    """Muestreador aleatorio de ventanas (x, y) desde archivos .bin en memmap.

    Args:
        data_dir: carpeta con los .bin y meta.json.
        block_size: longitud de contexto T.
        weights: dict fuente → peso absoluto. Si None, p ∝ tokens·repeat.
        repeat: dict fuente → repeat que pisa el de meta.json (ablaciones de mezcla
            sin re-tokenizar, p.ej. {"personal": 1}).
        seed: semilla del generador propio (reanudable y reproducible).
    """

    def __init__(self, data_dir: str | Path, block_size: int,
                 weights: dict[str, float] | None = None, repeat: dict[str, float] | None = None,
                 seed: int = 1337):
        self.data_dir = Path(data_dir)
        self.meta = json.loads((self.data_dir / "meta.json").read_text())
        self.dtype = np.dtype(self.meta["dtype"])
        self.block_size = block_size
        self.rng = np.random.default_rng(seed)

        self.train: dict[str, np.memmap] = {}
        raw_w: dict[str, float] = {}
        for src, info in self.meta["sources"].items():
            path = self.data_dir / f"train_{src}.bin"
            if not path.exists() or info["train_tokens"] <= block_size + 1:
                continue
            self.train[src] = np.memmap(path, dtype=self.dtype, mode="r")
            rep = (repeat or {}).get(src, info.get("repeat", 1))
            raw_w[src] = (weights or {}).get(src, info["train_tokens"] * rep)
        if not self.train:
            raise RuntimeError(f"No hay datos de entrenamiento en {self.data_dir}")
        total = sum(raw_w.values())
        self.sources = list(self.train)
        self.probs = np.array([raw_w[s] / total for s in self.sources])

        self.val: dict[str, np.memmap] = {}
        for split in ("val", "val_personal"):
            path = self.data_dir / f"{split}.bin"
            if path.exists() and path.stat().st_size > (block_size + 2) * self.dtype.itemsize:
                self.val[split] = np.memmap(path, dtype=self.dtype, mode="r")

    def mixture(self) -> dict[str, float]:
        return {s: round(float(p), 4) for s, p in zip(self.sources, self.probs)}

    def _windows(self, arr: np.ndarray, n: int) -> tuple[torch.Tensor, torch.Tensor]:
        T = self.block_size
        ix = self.rng.integers(0, len(arr) - T - 1, size=n)
        x = np.stack([arr[i:i + T].astype(np.int64) for i in ix])
        y = np.stack([arr[i + 1:i + T + 1].astype(np.int64) for i in ix])
        return torch.from_numpy(x), torch.from_numpy(y)

    def get_batch(self, batch_size: int, split: str = "train") -> tuple[torch.Tensor, torch.Tensor]:
        """Devuelve (x, y) de shape (B, T) en CPU (int64)."""
        if split != "train":
            return self._windows(self.val[split], batch_size)
        picks = self.rng.choice(len(self.sources), size=batch_size, p=self.probs)
        xs, ys = [], []
        for k in np.unique(picks):
            x, y = self._windows(self.train[self.sources[k]], int((picks == k).sum()))
            xs.append(x)
            ys.append(y)
        x, y = torch.cat(xs), torch.cat(ys)
        perm = torch.randperm(batch_size)
        return x[perm], y[perm]

    def state_dict(self) -> dict:
        return {"rng": self.rng.bit_generator.state}

    def load_state_dict(self, state: dict) -> None:
        self.rng.bit_generator.state = state["rng"]
