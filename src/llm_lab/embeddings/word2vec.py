"""Word2Vec skip-gram con negative sampling, desde cero (Fase 4).

Objetivo skip-gram: dada una palabra central, predecir sus vecinas. El softmax
sobre todo el vocabulario es intratable (O(V) por paso), así que se sustituye
por negative sampling: para cada par positivo (centro, contexto) se muestrean k
"negativos" y se entrena un clasificador binario:

    L = -log σ(v_c · v_o) - Σ_{i=1..k} log σ(-v_c · v_{n_i})

donde σ es la sigmoide. Los negativos se muestrean de una distribución
proporcional a f(w)^0.75 (suaviza las frecuencias: da algo más de peso a las
palabras raras que la frecuencia cruda).
"""

from __future__ import annotations

import numpy as np
import torch
import torch.nn.functional as F
from torch import nn

__all__ = ["SkipGramModel", "build_vocab", "build_training_pairs", "negative_sampling_table"]


def build_vocab(tokenized_sentences, min_count: int = 1) -> tuple[dict, dict, np.ndarray]:
    """Construye word->id, id->word y el array de frecuencias."""
    from collections import Counter

    counts = Counter(w for sent in tokenized_sentences for w in sent)
    vocab = [w for w, c in counts.items() if c >= min_count]
    word2id = {w: i for i, w in enumerate(vocab)}
    id2word = {i: w for w, i in word2id.items()}
    freqs = np.array([counts[w] for w in vocab], dtype=np.float64)
    return word2id, id2word, freqs


def negative_sampling_table(freqs: np.ndarray, power: float = 0.75) -> np.ndarray:
    """Distribución de muestreo de negativos ∝ freq^power, normalizada."""
    p = freqs ** power
    return p / p.sum()


def build_training_pairs(
    tokenized_sentences, word2id: dict, window: int = 2, subsample_t: float | None = 1e-3, freqs: np.ndarray | None = None
) -> list[tuple[int, int]]:
    """Genera pares (centro, contexto) con ventana y subsampling opcional.

    Subsampling (Mikolov 2013b): descarta palabras muy frecuentes con prob
    1 - sqrt(t / f), reduciendo el dominio de stopwords sobre el entrenamiento.
    """
    keep_prob = None
    if subsample_t is not None and freqs is not None:
        total = freqs.sum()
        f = freqs / total
        keep_prob = np.minimum(1.0, np.sqrt(subsample_t / f) + subsample_t / f)

    pairs = []
    for sent in tokenized_sentences:
        ids = [word2id[w] for w in sent if w in word2id]
        if keep_prob is not None:
            ids = [i for i in ids if np.random.rand() < keep_prob[i]]
        for pos, center in enumerate(ids):
            lo = max(0, pos - window)
            hi = min(len(ids), pos + window + 1)
            for ctx_pos in range(lo, hi):
                if ctx_pos != pos:
                    pairs.append((center, ids[ctx_pos]))
    return pairs


class SkipGramModel(nn.Module):
    """Skip-gram con negative sampling. Dos matrices de embedding (in/out)."""

    def __init__(self, vocab_size: int, dim: int = 100):
        super().__init__()
        self.in_emb = nn.Embedding(vocab_size, dim)
        self.out_emb = nn.Embedding(vocab_size, dim)
        nn.init.uniform_(self.in_emb.weight, -0.5 / dim, 0.5 / dim)
        nn.init.zeros_(self.out_emb.weight)

    def forward(self, center: torch.Tensor, context: torch.Tensor, negatives: torch.Tensor) -> torch.Tensor:
        """center: (B,), context: (B,), negatives: (B, k). Devuelve la loss escalar."""
        v_c = self.in_emb(center)                 # (B, d)
        v_o = self.out_emb(context)               # (B, d)
        v_n = self.out_emb(negatives)             # (B, k, d)

        pos_score = torch.sum(v_c * v_o, dim=1)               # (B,)
        pos_loss = F.logsigmoid(pos_score)
        neg_score = torch.bmm(v_n, v_c.unsqueeze(2)).squeeze(2)  # (B, k)
        neg_loss = F.logsigmoid(-neg_score).sum(1)
        return -(pos_loss + neg_loss).mean()

    def embeddings(self) -> torch.Tensor:
        """Embeddings finales (convención: la matriz de entrada)."""
        return self.in_emb.weight.detach()
