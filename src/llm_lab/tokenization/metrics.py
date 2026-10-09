"""Métricas de calidad de un tokenizador (Fase 2).

Permiten comparar tokenizadores objetivamente: cuántos tokens gasta por
palabra (fertilidad), cuánto comprime el texto, qué tan bien cubre el
vocabulario técnico del corpus, y la entropía de la distribución de tokens.
"""

from __future__ import annotations

import math
from collections import Counter
from typing import Callable, Sequence

__all__ = [
    "fertility",
    "compression",
    "vocab_coverage",
    "token_entropy",
]

# Una función de encode: texto -> lista de ids (o de tokens). Cualquier
# callable que devuelva una secuencia indexable sirve (HF, BPE propio...).
EncodeFn = Callable[[str], Sequence]


def fertility(texts: Sequence[str], encode: EncodeFn) -> float:
    """Tokens por palabra (separando por espacios en blanco).

    Fertilidad ≈ 1.0 significa ~1 token por palabra (muy eficiente para ese
    idioma); valores altos indican que el tokenizador fragmenta mucho —típico
    en idiomas o jerga técnica poco representados en su corpus de entrenamiento.
    """
    n_tokens = sum(len(encode(t)) for t in texts)
    n_words = sum(len(t.split()) for t in texts)
    return n_tokens / max(n_words, 1)


def compression(texts: Sequence[str], encode: EncodeFn) -> dict[str, float]:
    """Ratios de compresión: caracteres/token y bytes/token.

    Más caracteres por token = secuencias más cortas = más texto cabe en la
    ventana de contexto del LLM. Es una métrica directa de eficiencia.
    """
    n_tokens = sum(len(encode(t)) for t in texts)
    n_chars = sum(len(t) for t in texts)
    n_bytes = sum(len(t.encode("utf-8")) for t in texts)
    n_tokens = max(n_tokens, 1)
    return {
        "chars_per_token": n_chars / n_tokens,
        "bytes_per_token": n_bytes / n_tokens,
    }


def vocab_coverage(terms: Sequence[str], encode: EncodeFn) -> dict[str, float]:
    """Fracción de términos clave que se tokenizan en UN solo token.

    Para un LLM técnico interesa que términos como "subestación" o "gradiente"
    sean un único token: se aprenden y generan con mayor fidelidad que si
    quedan partidos en sub-fragmentos.
    """
    single = sum(1 for term in terms if len(encode(term)) == 1)
    lengths = [len(encode(term)) for term in terms]
    return {
        "single_token_ratio": single / max(len(terms), 1),
        "avg_tokens_per_term": sum(lengths) / max(len(lengths), 1),
    }


def token_entropy(token_ids: Sequence[int], base: float = 2.0) -> float:
    """Entropía (en bits si base=2) de la distribución empírica de tokens.

    H = -Σ p_i log_b(p_i). Acotada por log_b(V_observado): cuanto más
    uniforme el uso de tokens, mayor la entropía. Útil para detectar
    vocabularios infrautilizados (entropía muy por debajo del máximo).
    """
    counts = Counter(token_ids)
    total = sum(counts.values())
    if total == 0:
        return 0.0
    h = -sum((c / total) * math.log(c / total, base) for c in counts.values())
    return h
