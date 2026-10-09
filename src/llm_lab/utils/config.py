"""Carga de configuración modular: base.yaml + perfil (small/large) + overrides.

Patrón de configuración en capas (igual que Hydra/OmegaConf pero sin
dependencias extra): los valores más específicos pisan a los más generales.

    base.yaml  <-  small.yaml | large.yaml  <-  overrides en código

Uso típico en un notebook:

    from llm_lab.utils.config import load_config
    cfg = load_config(profile="small", overrides={"training": {"max_steps": 100}})
    cfg["model"]["d_model"]   # -> 256
"""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

import yaml

# Raíz del repo: src/llm_lab/utils/config.py -> tres niveles arriba
_REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_DIR = _REPO_ROOT / "configs"


def _deep_merge(base: dict, override: dict) -> dict:
    """Fusiona ``override`` sobre ``base`` recursivamente (sin mutar inputs)."""
    result = copy.deepcopy(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = copy.deepcopy(value)
    return result


def load_yaml(name: str, config_dir: str | Path | None = None) -> dict[str, Any]:
    """Carga un YAML de configs/ por nombre (con o sin extensión)."""
    directory = Path(config_dir) if config_dir else CONFIG_DIR
    path = directory / (name if name.endswith(".yaml") else f"{name}.yaml")
    if not path.exists():
        raise FileNotFoundError(f"No existe el config: {path}")
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_config(
    base: str = "base",
    profile: str | None = None,
    overrides: dict[str, Any] | None = None,
    config_dir: str | Path | None = None,
) -> dict[str, Any]:
    """Carga configuración en capas: base <- perfil <- overrides.

    Args:
        base: nombre del YAML base (default "base").
        profile: "small" | "large" | None. Si None, no aplica perfil.
        overrides: dict con valores que pisan todo lo anterior.
        config_dir: directorio alternativo de configs (para tests).
    """
    cfg = load_yaml(base, config_dir)
    if profile:
        cfg = _deep_merge(cfg, load_yaml(profile, config_dir))
    if overrides:
        cfg = _deep_merge(cfg, overrides)
    return cfg
