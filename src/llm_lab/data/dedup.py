"""Deduplicación exacta (SHA-256) y aproximada (MinHash + LSH) — Fase 3.

Dos niveles, igual que los pipelines de corpus reales (Gopher, RefinedWeb):

1. **Exacta**: hash SHA-256 del texto normalizado. Atrapa copias literales.
2. **Near-dedup**: MinHash estima la similitud de Jaccard entre conjuntos
   de n-gramas (shingles) sin comparar todos los pares; LSH (Locality
   Sensitive Hashing) por bandas indexa las firmas para encontrar
   candidatos en tiempo ~O(1) por documento.

**Intuición de MinHash**: para una permutación aleatoria π del universo de
shingles, P(min π(A) == min π(B)) = |A∩B| / |A∪B| = Jaccard(A, B).
Con k permutaciones independientes, la fracción de mínimos que coinciden
es un estimador insesgado de la similitud de Jaccard. En lugar de permutar
explícitamente, aplicamos k funciones hash distintas (hash con sal) y
tomamos el mínimo de cada una.

**Intuición de LSH por bandas**: la firma de k valores se parte en b bandas
de r filas (k = b·r). Dos documentos son candidatos si coinciden en TODAS
las filas de al menos una banda. P(candidato) = 1 - (1 - s^r)^b — una
curva en S con umbral ≈ (1/b)^(1/r).
"""

from __future__ import annotations

import hashlib
import struct
from collections import defaultdict
from collections.abc import Iterable

__all__ = [
    "sha256_hash",
    "exact_dedup",
    "shingles",
    "minhash_signature",
    "jaccard_estimate",
    "LSHIndex",
]


def sha256_hash(text: str) -> str:
    """SHA-256 hexadecimal del texto (UTF-8)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exact_dedup(texts: Iterable[str]) -> tuple[list[str], list[int]]:
    """Elimina duplicados exactos por hash SHA-256, preservando el orden.

    Args:
        texts: textos (idealmente ya normalizados con
            :func:`llm_lab.data.cleaning.normalize_text`).

    Returns:
        Tupla ``(unique_texts, duplicate_indices)``: los textos únicos en
        orden de primera aparición y los índices originales descartados.
    """
    seen: set[str] = set()
    unique: list[str] = []
    duplicates: list[int] = []
    for i, text in enumerate(texts):
        digest = sha256_hash(text)
        if digest in seen:
            duplicates.append(i)
        else:
            seen.add(digest)
            unique.append(text)
    return unique, duplicates


def shingles(text: str, n: int = 3) -> set[str]:
    """Conjunto de n-gramas de palabras (shingles) de un texto.

    Usamos n-gramas de PALABRAS (no de caracteres) porque el corpus es
    texto técnico largo: 3-gramas de palabras dan buena señal de copia
    sin explotar en cardinalidad.

    Args:
        text: texto de entrada.
        n: tamaño del n-grama (default 3).

    Returns:
        Set de shingles como strings "w1 w2 w3". Si el texto tiene menos
        de ``n`` palabras, devuelve un único shingle con todas ellas.
    """
    words = text.lower().split()
    if len(words) < n:
        return {" ".join(words)} if words else set()
    return {" ".join(words[i : i + n]) for i in range(len(words) - n + 1)}


def _hash_with_salt(shingle: str, salt: int) -> int:
    """Hash de 64 bits del shingle con una 'sal' que simula la permutación k."""
    h = hashlib.blake2b(shingle.encode("utf-8"), digest_size=8, salt=struct.pack("<q", salt))
    return int.from_bytes(h.digest(), "little")


def minhash_signature(shingle_set: set[str], num_perm: int = 128) -> list[int]:
    """Firma MinHash: el mínimo de cada una de las k funciones hash.

    Cada función hash (blake2b con sal distinta) simula una permutación
    aleatoria del universo de shingles; el mínimo bajo esa permutación es
    el 'representante' del conjunto.

    Args:
        shingle_set: conjunto de shingles del documento.
        num_perm: número de permutaciones/hashes k (default 128, como
            ``deduplication.near.num_perm`` en configs/corpus.yaml).

    Returns:
        Lista de k enteros de 64 bits. Para un set vacío, k veces el
        máximo entero (firma que no colisiona con nada).
    """
    max_u64 = (1 << 64) - 1
    if not shingle_set:
        return [max_u64] * num_perm
    signature = []
    for salt in range(num_perm):
        signature.append(min(_hash_with_salt(s, salt) for s in shingle_set))
    return signature


def jaccard_estimate(sig_a: list[int], sig_b: list[int]) -> float:
    """Estima Jaccard(A, B) como la fracción de posiciones coincidentes.

    El estimador es insesgado con varianza ≈ s(1-s)/k, así que con k=128
    el error estándar es < 0.05 para cualquier similitud.
    """
    if len(sig_a) != len(sig_b):
        raise ValueError(f"Firmas de distinto tamaño: {len(sig_a)} vs {len(sig_b)}")
    if not sig_a:
        return 0.0
    return sum(a == b for a, b in zip(sig_a, sig_b)) / len(sig_a)


class LSHIndex:
    """Índice LSH por bandas para encontrar candidatos a near-duplicados.

    La firma de ``num_perm`` valores se parte en ``num_bands`` bandas de
    ``num_perm // num_bands`` filas. Dos documentos son candidatos si
    alguna banda completa coincide. El umbral efectivo de similitud es
    aproximadamente ``(1/b)^(1/r)`` — con 128 permutaciones y 32 bandas
    (r=4), umbral ≈ 0.42; con 16 bandas (r=8), umbral ≈ 0.70.

    Uso::

        index = LSHIndex(num_perm=128, num_bands=16)
        for doc_id, text in docs:
            sig = minhash_signature(shingles(text))
            candidates = index.query(sig)      # ids ya indexados similares
            index.add(doc_id, sig)
    """

    def __init__(self, num_perm: int = 128, num_bands: int = 16) -> None:
        if num_perm % num_bands != 0:
            raise ValueError(f"num_perm ({num_perm}) debe ser divisible por num_bands ({num_bands})")
        self.num_perm = num_perm
        self.num_bands = num_bands
        self.rows_per_band = num_perm // num_bands
        # Un dict por banda: tupla de la banda -> ids de documentos.
        self._buckets: list[dict[tuple[int, ...], list[str]]] = [
            defaultdict(list) for _ in range(num_bands)
        ]
        self.signatures: dict[str, list[int]] = {}

    def _band_keys(self, signature: list[int]) -> list[tuple[int, ...]]:
        """Parte la firma en tuplas hashables, una por banda."""
        r = self.rows_per_band
        return [tuple(signature[b * r : (b + 1) * r]) for b in range(self.num_bands)]

    def add(self, doc_id: str, signature: list[int]) -> None:
        """Indexa la firma de un documento bajo sus claves de banda."""
        if len(signature) != self.num_perm:
            raise ValueError(f"Firma de tamaño {len(signature)}, se esperaba {self.num_perm}")
        self.signatures[doc_id] = signature
        for band, key in enumerate(self._band_keys(signature)):
            self._buckets[band][key].append(doc_id)

    def query(self, signature: list[int]) -> set[str]:
        """Devuelve los ids candidatos (≥ 1 banda en común con la firma)."""
        candidates: set[str] = set()
        for band, key in enumerate(self._band_keys(signature)):
            candidates.update(self._buckets[band].get(key, ()))
        return candidates

    def find_duplicates(self, signature: list[int], threshold: float = 0.85) -> list[tuple[str, float]]:
        """Candidatos filtrados por similitud Jaccard estimada ≥ threshold.

        LSH solo da candidatos (con falsos positivos); aquí se verifica
        cada uno con :func:`jaccard_estimate` antes de declararlo duplicado.
        """
        results = []
        for doc_id in self.query(signature):
            sim = jaccard_estimate(signature, self.signatures[doc_id])
            if sim >= threshold:
                results.append((doc_id, sim))
        return sorted(results, key=lambda pair: -pair[1])
