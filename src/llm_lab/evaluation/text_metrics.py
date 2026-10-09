"""Métricas de texto educacionales: BLEU y ROUGE-L desde cero (Fase 8).

Implementaciones puras en Python para ENTENDER las métricas. Para resultados
publicables usar ``sacrebleu`` y ``rouge-score`` (tokenización y casos límite
estandarizados), como se muestra en el notebook 08.
"""

from __future__ import annotations

import math
from collections import Counter

__all__ = ["bleu_score", "rouge_l", "ngram_counts", "lcs_length"]


def ngram_counts(tokens: list[str], n: int) -> Counter:
    """Cuenta los n-gramas de una lista de tokens."""
    return Counter(tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1))


def bleu_score(candidate: list[str], reference: list[str], max_n: int = 4) -> float:
    """BLEU con una sola referencia.

    Precisión de n-gramas modificada (con clipping al conteo de la referencia),
    media geométrica de n=1..max_n, y brevity penalty que castiga candidatos
    más cortos que la referencia.
    """
    if len(candidate) == 0:
        return 0.0
    precisions = []
    for n in range(1, max_n + 1):
        cand_ngrams = ngram_counts(candidate, n)
        ref_ngrams = ngram_counts(reference, n)
        if not cand_ngrams:
            precisions.append(0.0)
            continue
        # Clipping: cada n-grama del candidato cuenta hasta el máximo de la ref.
        clipped = sum(min(c, ref_ngrams.get(g, 0)) for g, c in cand_ngrams.items())
        total = sum(cand_ngrams.values())
        precisions.append(clipped / total)

    if min(precisions) == 0:
        geo_mean = 0.0
    else:
        geo_mean = math.exp(sum(math.log(p) for p in precisions) / max_n)

    # Brevity penalty.
    c, r = len(candidate), len(reference)
    bp = 1.0 if c > r else math.exp(1 - r / max(c, 1))
    return bp * geo_mean


def lcs_length(a: list[str], b: list[str]) -> int:
    """Longitud de la subsecuencia común más larga (LCS) por programación dinámica."""
    m, k = len(a), len(b)
    dp = [[0] * (k + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, k + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][k]


def rouge_l(candidate: list[str], reference: list[str], beta: float = 1.2) -> dict[str, float]:
    """ROUGE-L basada en LCS: precision, recall y F (favorece recall si beta>1)."""
    lcs = lcs_length(candidate, reference)
    prec = lcs / max(len(candidate), 1)
    rec = lcs / max(len(reference), 1)
    if prec + rec == 0:
        f = 0.0
    else:
        f = (1 + beta**2) * prec * rec / (rec + beta**2 * prec)
    return {"precision": prec, "recall": rec, "f": f, "lcs": lcs}
