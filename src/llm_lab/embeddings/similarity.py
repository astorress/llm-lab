"""Similitud y aritmética en espacios de embeddings (Fase 4)."""

from __future__ import annotations

import numpy as np

__all__ = ["cosine_similarity_matrix", "nearest_neighbors", "analogy"]


def _to_numpy(x):
    return x.detach().cpu().numpy() if hasattr(x, "detach") else np.asarray(x)


def cosine_similarity_matrix(vectors) -> np.ndarray:
    """Matriz (N, N) de similitudes coseno entre todos los vectores."""
    v = _to_numpy(vectors).astype(np.float64)
    norm = np.linalg.norm(v, axis=1, keepdims=True)
    norm[norm == 0] = 1e-12
    unit = v / norm
    return unit @ unit.T


def nearest_neighbors(vectors, word2id: dict, id2word: dict, query: str, k: int = 5):
    """Devuelve los k vecinos más cercanos por coseno a ``query`` (excluyéndola)."""
    if query not in word2id:
        raise KeyError(f"'{query}' no está en el vocabulario")
    v = _to_numpy(vectors).astype(np.float64)
    norm = np.linalg.norm(v, axis=1, keepdims=True)
    norm[norm == 0] = 1e-12
    unit = v / norm
    qi = word2id[query]
    sims = unit @ unit[qi]
    order = np.argsort(-sims)
    out = []
    for idx in order:
        if idx == qi:
            continue
        out.append((id2word[idx], float(sims[idx])))
        if len(out) >= k:
            break
    return out


def analogy(vectors, word2id: dict, id2word: dict, a: str, b: str, c: str, k: int = 3):
    """Resuelve 'a es a b como c es a ?' con 3CosAdd: b - a + c.

    Ejemplo: rey - hombre + mujer ≈ reina; voltaje - corriente + caudal ≈ presión.
    """
    v = _to_numpy(vectors).astype(np.float64)
    for w in (a, b, c):
        if w not in word2id:
            raise KeyError(f"'{w}' no está en el vocabulario")
    target = v[word2id[b]] - v[word2id[a]] + v[word2id[c]]
    norm = np.linalg.norm(v, axis=1, keepdims=True)
    norm[norm == 0] = 1e-12
    unit = v / norm
    target = target / (np.linalg.norm(target) + 1e-12)
    sims = unit @ target
    exclude = {word2id[a], word2id[b], word2id[c]}
    order = np.argsort(-sims)
    out = []
    for idx in order:
        if idx in exclude:
            continue
        out.append((id2word[idx], float(sims[idx])))
        if len(out) >= k:
            break
    return out
