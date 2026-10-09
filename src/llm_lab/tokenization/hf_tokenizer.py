"""Entrenamiento de un tokenizador byte-level BPE con la librería `tokenizers` (Fase 2).

A diferencia de :mod:`llm_lab.tokenization.bpe` (educacional, Python puro,
sobre caracteres Unicode), aquí se entrena el tokenizador *de producción*:
byte-level BPE (igual que GPT-2/Llama), implementado en Rust, con
normalización NFKC y tokens especiales.

La dependencia ``tokenizers`` se importa de forma perezosa dentro de las
funciones para que el paquete sea importable sin tenerla instalada.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

__all__ = ["train_bpe_tokenizer", "load_tokenizer", "DEFAULT_SPECIAL_TOKENS"]

# Tokens especiales del laboratorio. <|endoftext|> separa documentos durante
# el pre-entrenamiento (packing); los de chat se usan en fine-tuning (Fase 7).
DEFAULT_SPECIAL_TOKENS = [
    "<|endoftext|>",
    "<|pad|>",
    "<|im_start|>",
    "<|im_end|>",
]


def train_bpe_tokenizer(
    corpus: Iterable[str],
    vocab_size: int = 8000,
    min_frequency: int = 2,
    special_tokens: list[str] | None = None,
    save_path: str | Path | None = None,
):
    """Entrena un ByteLevel BPE sobre un iterable de textos.

    Args:
        corpus: iterable de documentos (str).
        vocab_size: tamaño objetivo del vocabulario (8k SMALL, 32k LARGE).
        min_frequency: frecuencia mínima de un par para fusionarse.
        special_tokens: tokens especiales; por defecto ``DEFAULT_SPECIAL_TOKENS``.
        save_path: si se indica, guarda el tokenizador como JSON.

    Returns:
        El objeto ``tokenizers.Tokenizer`` entrenado.
    """
    from tokenizers import Tokenizer, decoders, pre_tokenizers, processors, trainers
    from tokenizers.models import BPE
    from tokenizers.normalizers import NFKC

    specials = special_tokens or DEFAULT_SPECIAL_TOKENS

    tokenizer = Tokenizer(BPE(unk_token=None))
    tokenizer.normalizer = NFKC()
    # add_prefix_space=False evita un espacio fantasma al inicio del texto.
    tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
    tokenizer.decoder = decoders.ByteLevel()
    tokenizer.post_processor = processors.ByteLevel(trim_offsets=True)

    trainer = trainers.BpeTrainer(
        vocab_size=vocab_size,
        min_frequency=min_frequency,
        special_tokens=specials,
        # El alfabeto inicial son los 256 bytes: garantiza que NUNCA haya UNK.
        initial_alphabet=pre_tokenizers.ByteLevel.alphabet(),
        show_progress=True,
    )

    tokenizer.train_from_iterator(corpus, trainer=trainer)

    if save_path is not None:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        tokenizer.save(str(save_path))

    return tokenizer


def load_tokenizer(path: str | Path):
    """Carga un tokenizador previamente entrenado desde su JSON."""
    from tokenizers import Tokenizer

    return Tokenizer.from_file(str(path))
