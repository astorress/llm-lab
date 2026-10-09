"""Rutas y helpers compartidos por los scripts del pipeline de entrenamiento.

Pipeline (cada paso escribe en una carpeta por perfil, así tiny/small/large
conviven sin pisarse):

    collect_personal_corpus  → datasets/raw/personal/personal.jsonl
    build_corpus (semilla)   → datasets/processed/corpus.jsonl
    build_pretrain_corpus    → datasets/pretrain/<perfil>/<fuente>.jsonl.gz
    train_tokenizer          → tokenizer/trained/<perfil>/tokenizer.json
    tokenize_corpus          → datasets/tokenized/<perfil>/*.bin + meta.json
    pretrain                 → checkpoints/<perfil>/{last,best}.pt + logs/
    sft                      → checkpoints/<perfil>-sft/
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import yaml

from llm_lab.utils.config import load_config, load_yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]

__all__ = ["PROJECT_ROOT", "ProfilePaths", "load_profile", "load_data_config", "build_model_config"]


@dataclass
class ProfilePaths:
    profile: str
    pretrain: Path
    tokenizer: Path
    tokenized: Path
    checkpoints: Path

    @classmethod
    def for_profile(cls, profile: str, root: Path = PROJECT_ROOT) -> ProfilePaths:
        # LLM_LAB_DATA permite apuntar los artefactos pesados a Google Drive /
        # un volumen de Kaggle sin mover el código.
        data_root = Path(os.environ.get("LLM_LAB_DATA", root))
        return cls(
            profile=profile,
            pretrain=data_root / "datasets" / "pretrain" / profile,
            tokenizer=data_root / "tokenizer" / "trained" / profile / "tokenizer.json",
            tokenized=data_root / "datasets" / "tokenized" / profile,
            checkpoints=data_root / "checkpoints" / profile,
        )


def load_profile(profile: str) -> dict:
    """base.yaml ← <perfil>.yaml."""
    return load_config("base", profile=profile)


def load_data_config(profile: str) -> tuple[dict, dict[str, dict]]:
    """Devuelve (config global de datos, {fuente: spec}) para el perfil."""
    cfg = load_yaml("data")
    prof = cfg["profiles"][profile]
    names = list(cfg["sources"]) if prof["sources"] == "all" else prof["sources"]
    return cfg | {"total_tokens": prof["total_tokens"]}, {n: cfg["sources"][n] for n in names}


def build_model_config(cfg: dict, vocab_size: int | None = None):
    """GPTConfig desde la sección ``model`` del perfil."""
    from llm_lab.model.gpt import GPTConfig

    m = dict(cfg["model"])
    if vocab_size is not None:
        m["vocab_size"] = vocab_size
    fields = GPTConfig.__dataclass_fields__
    return GPTConfig(**{k: v for k, v in m.items() if k in fields})


def dump_yaml(obj, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(obj, sort_keys=False, allow_unicode=True), encoding="utf-8")
