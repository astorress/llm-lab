"""Estrategias de chunking del corpus (Fase 3): fixed, sentence y semantic.

Un LLM se entrena con secuencias de longitud fija (``max_seq_len``), pero
los documentos son de longitud arbitraria. El chunking decide DÓNDE cortar:

- ``chunk_fixed``: corta por número de tokens (aproximados) con overlap.
  Simple y rápido; puede partir oraciones por la mitad.
- ``chunk_sentences``: agrupa oraciones completas hasta llenar el budget.
  Nunca rompe una oración.
- ``chunk_semantic``: corta donde la similitud entre oraciones contiguas
  cae (cambio de tema). La función de similitud se INYECTA, así el módulo
  no depende de ningún modelo de embeddings concreto.

La cuenta de tokens es APROXIMADA (palabras × factor): suficiente para
balancear tamaños de chunk sin requerir el tokenizador entrenado, que es
de la Fase 2 y crearía una dependencia circular.
"""

from __future__ import annotations

import re
from collections.abc import Callable

__all__ = [
    "approx_token_count",
    "split_sentences",
    "chunk_fixed",
    "chunk_sentences",
    "chunk_semantic",
]

# Para texto técnico es/en con BPE de 8k-32k, ~1.3 tokens por palabra es
# una aproximación razonable (medible luego con tokenization.metrics.fertility).
TOKENS_PER_WORD = 1.3

# Fin de oración: . ! ? seguidos de espacio y mayúscula/dígito, o salto de línea.
_SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ0-9¿¡])|\n{2,}")


def approx_token_count(text: str, tokens_per_word: float = TOKENS_PER_WORD) -> int:
    """Estima el número de tokens de un texto: palabras × factor."""
    return max(1, round(len(text.split()) * tokens_per_word)) if text.strip() else 0


def split_sentences(text: str) -> list[str]:
    """Divide un texto en oraciones con una regex simple es/en.

    Heurística educacional (no maneja abreviaturas tipo "Dr."); para
    producción usar un segmentador real (spaCy, nltk punkt).
    """
    sentences = [s.strip() for s in _SENTENCE_END.split(text)]
    return [s for s in sentences if s]


def chunk_fixed(
    text: str,
    target_tokens: int = 512,
    overlap_tokens: int = 64,
    tokens_per_word: float = TOKENS_PER_WORD,
) -> list[str]:
    """Chunking por ventana fija de tokens aproximados, con overlap.

    Convierte el budget de tokens a palabras (tokens / factor) y desliza
    una ventana con solapamiento para no perder contexto en los bordes.

    Args:
        text: documento completo.
        target_tokens: tamaño objetivo de cada chunk en tokens.
        overlap_tokens: tokens compartidos entre chunks consecutivos.
        tokens_per_word: factor de conversión token/palabra.

    Returns:
        Lista de chunks (strings). Documento corto -> un solo chunk.
    """
    if overlap_tokens >= target_tokens:
        raise ValueError("overlap_tokens debe ser menor que target_tokens")
    words = text.split()
    words_per_chunk = max(1, int(target_tokens / tokens_per_word))
    overlap_words = int(overlap_tokens / tokens_per_word)
    step = max(1, words_per_chunk - overlap_words)

    if len(words) <= words_per_chunk:
        return [text.strip()] if text.strip() else []

    chunks = []
    for start in range(0, len(words), step):
        piece = words[start : start + words_per_chunk]
        chunks.append(" ".join(piece))
        if start + words_per_chunk >= len(words):
            break
    return chunks


def chunk_sentences(
    text: str,
    target_tokens: int = 512,
    tokens_per_word: float = TOKENS_PER_WORD,
) -> list[str]:
    """Chunking por oraciones completas: acumula hasta llenar el budget.

    Nunca corta una oración por la mitad. Si una sola oración excede el
    budget, va sola en su propio chunk (no se trocea).
    """
    sentences = split_sentences(text)
    if not sentences:
        return []

    chunks: list[str] = []
    current: list[str] = []
    current_tokens = 0
    for sentence in sentences:
        n_tokens = approx_token_count(sentence, tokens_per_word)
        if current and current_tokens + n_tokens > target_tokens:
            chunks.append(" ".join(current))
            current, current_tokens = [], 0
        current.append(sentence)
        current_tokens += n_tokens
    if current:
        chunks.append(" ".join(current))
    return chunks


def chunk_semantic(
    text: str,
    similarity_fn: Callable[[str, str], float],
    target_tokens: int = 512,
    similarity_threshold: float = 0.5,
    tokens_per_word: float = TOKENS_PER_WORD,
) -> list[str]:
    """Chunking semántico: corta donde cae la similitud entre oraciones.

    Recorre las oraciones acumulando; cierra el chunk cuando ocurre alguna
    de las dos condiciones:
    1. La similitud entre la oración anterior y la actual cae por debajo
       de ``similarity_threshold`` (cambio de tema), o
    2. Se excede ``target_tokens`` (límite duro de tamaño).

    La función de similitud se inyecta para mantener este módulo libre de
    dependencias de modelos. Ejemplos de ``similarity_fn``:

    - Jaccard de palabras (cero dependencias)::

        def jaccard(a, b):
            wa, wb = set(a.lower().split()), set(b.lower().split())
            return len(wa & wb) / max(1, len(wa | wb))

    - Coseno de embeddings (Fase 4)::

        sim = lambda a, b: cosine(embed(a), embed(b))

    Args:
        text: documento completo.
        similarity_fn: f(oración_a, oración_b) -> similitud en [0, 1].
        target_tokens: tamaño máximo del chunk en tokens aproximados.
        similarity_threshold: por debajo de esto se considera cambio de tema.
        tokens_per_word: factor de conversión token/palabra.

    Returns:
        Lista de chunks alineados con los límites temáticos.
    """
    sentences = split_sentences(text)
    if not sentences:
        return []

    chunks: list[str] = []
    current: list[str] = [sentences[0]]
    current_tokens = approx_token_count(sentences[0], tokens_per_word)

    for prev, sentence in zip(sentences, sentences[1:]):
        n_tokens = approx_token_count(sentence, tokens_per_word)
        topic_break = similarity_fn(prev, sentence) < similarity_threshold
        size_break = current_tokens + n_tokens > target_tokens
        if topic_break or size_break:
            chunks.append(" ".join(current))
            current, current_tokens = [], 0
        current.append(sentence)
        current_tokens += n_tokens

    if current:
        chunks.append(" ".join(current))
    return chunks
