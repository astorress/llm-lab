"""BPE (Byte Pair Encoding) educacional desde cero, en Python puro (Fase 2).

El algoritmo (Sennrich et al., 2016, adaptado de la compresión de Gage, 1994):

1. Partir cada palabra del corpus en caracteres (símbolos iniciales).
2. Contar la frecuencia de cada PAR de símbolos adyacentes.
3. Fusionar (merge) el par más frecuente en un símbolo nuevo.
4. Repetir hasta alcanzar ``vocab_size``.

Cada merge aprendido es una regla determinista; codificar un texto nuevo
es re-aplicar los merges en el MISMO orden en que se aprendieron.

Esta implementación opera sobre caracteres Unicode (no bytes) y prioriza
la legibilidad sobre la velocidad: O(vocab_size × corpus) por el reconteo
de pares en cada iteración. La versión industrial (byte-level, en Rust)
está en :mod:`llm_lab.tokenization.hf_tokenizer`.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

__all__ = ["BPETokenizer"]

# Marcador de fin de palabra: permite reconstruir los espacios en decode()
# y evita que un merge cruce el límite entre dos palabras.
_END_OF_WORD = "</w>"
_UNK = "<unk>"


class BPETokenizer:
    """Tokenizador BPE educacional: train / encode / decode / save / load.

    Atributos:
        vocab: dict símbolo -> id (incluye caracteres base y merges).
        merges: lista ordenada de pares fusionados [("t","h"), ("th","e"), ...].
            El ORDEN importa: encode() los aplica en orden de aprendizaje.
    """

    def __init__(self) -> None:
        self.vocab: dict[str, int] = {}
        self.merges: list[tuple[str, str]] = []
        self._id_to_token: dict[int, str] = {}
        # Ranking del par -> posición del merge (para encode rápido).
        self._merge_ranks: dict[tuple[str, str], int] = {}

    # ------------------------------------------------------------------
    # Entrenamiento
    # ------------------------------------------------------------------

    @staticmethod
    def _word_frequencies(corpus: list[str]) -> Counter[tuple[str, ...]]:
        """Cuenta palabras del corpus, cada una como tupla de símbolos.

        "the" -> ("t", "h", "e", "</w>"). Trabajar con frecuencias de
        palabra (no con el texto plano) hace el conteo de pares O(palabras
        únicas) en lugar de O(tokens del corpus).
        """
        freqs: Counter[tuple[str, ...]] = Counter()
        for text in corpus:
            for word in text.split():
                freqs[tuple(word) + (_END_OF_WORD,)] += 1
        return freqs

    @staticmethod
    def _count_pairs(word_freqs: Counter[tuple[str, ...]]) -> Counter[tuple[str, str]]:
        """Frecuencia de cada par de símbolos adyacentes, ponderada por palabra."""
        pairs: Counter[tuple[str, str]] = Counter()
        for word, freq in word_freqs.items():
            for left, right in zip(word, word[1:]):
                pairs[(left, right)] += freq
        return pairs

    @staticmethod
    def _merge_word(word: tuple[str, ...], pair: tuple[str, str]) -> tuple[str, ...]:
        """Aplica un merge a una palabra: reemplaza (a, b) adyacentes por 'ab'."""
        merged: list[str] = []
        i = 0
        while i < len(word):
            if i < len(word) - 1 and (word[i], word[i + 1]) == pair:
                merged.append(word[i] + word[i + 1])
                i += 2
            else:
                merged.append(word[i])
                i += 1
        return tuple(merged)

    def train(self, corpus: list[str], vocab_size: int = 1000, verbose: bool = False) -> None:
        """Aprende los merges BPE a partir de un corpus de textos.

        Args:
            corpus: lista de textos de entrenamiento.
            vocab_size: tamaño objetivo del vocabulario (caracteres base
                + merges + <unk>). El entrenamiento para antes si no
                quedan pares que fusionar.
            verbose: imprime cada merge aprendido (instructivo con corpus
                pequeños).
        """
        word_freqs = self._word_frequencies(corpus)
        if not word_freqs:
            raise ValueError("Corpus vacío: no hay nada que entrenar")

        # Vocabulario inicial: <unk> + todos los caracteres del corpus.
        symbols = {_UNK, _END_OF_WORD}
        for word in word_freqs:
            symbols.update(word)
        self.vocab = {tok: i for i, tok in enumerate(sorted(symbols))}
        self.merges = []

        while len(self.vocab) < vocab_size:
            pairs = self._count_pairs(word_freqs)
            if not pairs:
                break  # cada palabra es ya un solo símbolo
            best_pair, best_freq = pairs.most_common(1)[0]
            if best_freq < 2:
                break  # fusionar pares únicos solo memoriza el corpus

            self.merges.append(best_pair)
            new_symbol = best_pair[0] + best_pair[1]
            self.vocab[new_symbol] = len(self.vocab)
            if verbose:
                print(f"merge {len(self.merges):4d}: {best_pair} -> '{new_symbol}' (freq={best_freq})")

            # Re-segmentar las palabras afectadas con el nuevo merge.
            word_freqs = Counter(
                {self._merge_word(word, best_pair): freq for word, freq in word_freqs.items()}
            )

        self._rebuild_indices()

    def _rebuild_indices(self) -> None:
        """Reconstruye los índices derivados (id->token, ranking de merges)."""
        self._id_to_token = {i: tok for tok, i in self.vocab.items()}
        self._merge_ranks = {pair: rank for rank, pair in enumerate(self.merges)}

    # ------------------------------------------------------------------
    # Codificación / decodificación
    # ------------------------------------------------------------------

    def _encode_word(self, word: str) -> list[str]:
        """Segmenta una palabra aplicando los merges en orden de ranking.

        En cada paso se fusiona el par presente con MENOR ranking (el que
        se aprendió primero) — exactamente el criterio de GPT-2.
        """
        symbols = list(word) + [_END_OF_WORD]
        while len(symbols) > 1:
            # Par adyacente con mejor (menor) ranking de merge.
            best_rank, best_idx = None, None
            for i, pair in enumerate(zip(symbols, symbols[1:])):
                rank = self._merge_ranks.get(pair)
                if rank is not None and (best_rank is None or rank < best_rank):
                    best_rank, best_idx = rank, i
            if best_idx is None:
                break  # no queda ningún merge aplicable
            symbols[best_idx : best_idx + 2] = [symbols[best_idx] + symbols[best_idx + 1]]
        return symbols

    def encode(self, text: str) -> list[int]:
        """Codifica un texto a lista de ids. Símbolos desconocidos -> <unk>."""
        if not self.vocab:
            raise RuntimeError("Tokenizador sin entrenar: llamar a train() o load() primero")
        unk_id = self.vocab[_UNK]
        ids: list[int] = []
        for word in text.split():
            for symbol in self._encode_word(word):
                ids.append(self.vocab.get(symbol, unk_id))
        return ids

    def decode(self, ids: list[int]) -> str:
        """Reconstruye el texto: concatena tokens y convierte </w> en espacio."""
        text = "".join(self._id_to_token.get(i, _UNK) for i in ids)
        return text.replace(_END_OF_WORD, " ").strip()

    # ------------------------------------------------------------------
    # Persistencia
    # ------------------------------------------------------------------

    def save(self, path: str | Path) -> None:
        """Guarda vocab + merges como JSON legible."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "vocab": self.vocab,
            # JSON no tiene tuplas: se guardan como listas de 2 strings.
            "merges": [list(pair) for pair in self.merges],
        }
        with path.open("w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

    @classmethod
    def load(cls, path: str | Path) -> BPETokenizer:
        """Carga un tokenizador guardado con :meth:`save`."""
        with Path(path).open(encoding="utf-8") as f:
            payload = json.load(f)
        tokenizer = cls()
        tokenizer.vocab = {tok: int(i) for tok, i in payload["vocab"].items()}
        tokenizer.merges = [tuple(pair) for pair in payload["merges"]]
        tokenizer._rebuild_indices()
        return tokenizer

    def __len__(self) -> int:
        return len(self.vocab)
