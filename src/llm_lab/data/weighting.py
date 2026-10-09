"""Balanceo del corpus por dominio (Fase 3): sampling temperado.

Implementa la fórmula de muestreo multi-dominio usada en LLMs reales
(multilingual BERT, XLM-R, Gopher con sus pesos por fuente):

    P(d) ∝ w_d · n_d^α

donde:
- ``n_d`` = número de documentos (o tokens) del dominio d,
- ``w_d`` = peso manual del dominio (configs/corpus.yaml),
- ``α``   = temperatura de muestreo. α=1 reproduce la distribución
  natural (los dominios grandes dominan); α=0 uniformiza por completo;
  α=0.7 (default, el valor de mBERT/XLM-R) sube los dominios pequeños
  sin aplanar del todo los grandes.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from llm_lab.utils.config import load_yaml

__all__ = ["load_domain_weights", "domain_sampling_probs"]


def load_domain_weights(config_dir: str | Path | None = None) -> dict[str, float]:
    """Lee los pesos manuales w_d de configs/corpus.yaml.

    Returns:
        Dict dominio -> peso (p.ej. {"machine_learning": 1.5, ...}).
    """
    corpus_cfg = load_yaml("corpus", config_dir)
    domains = corpus_cfg.get("domains", {})
    return {name: float(spec.get("weight", 1.0)) for name, spec in domains.items()}


def domain_sampling_probs(
    domain_counts: Mapping[str, int],
    alpha: float = 0.7,
    weights: Mapping[str, float] | None = None,
    config_dir: str | Path | None = None,
) -> dict[str, float]:
    """Probabilidades de muestreo por dominio: P(d) ∝ w_d · n_d^α.

    Args:
        domain_counts: dominio -> número de documentos (o tokens) n_d.
            Dominios con n_d <= 0 reciben probabilidad 0.
        alpha: temperatura de muestreo en [0, 1]. Default 0.7.
        weights: pesos manuales w_d; si None se cargan de
            configs/corpus.yaml. Dominios sin peso definido usan 1.0.
        config_dir: directorio alternativo de configs (para tests).

    Returns:
        Dict dominio -> probabilidad, normalizado para sumar 1.0.

    Ejemplo::

        >>> probs = domain_sampling_probs({"python": 1000, "mongodb": 10})
        >>> # Con α=0.7, mongodb pasa de 1% natural a ~4.6%: los dominios
        >>> # pequeños se sobremuestrean sin aplastar a los grandes.
    """
    if not 0.0 <= alpha <= 1.0:
        raise ValueError(f"alpha debe estar en [0, 1], recibido {alpha}")
    if weights is None:
        weights = load_domain_weights(config_dir)

    # Score no normalizado: w_d * n_d^alpha (0 si el dominio está vacío).
    scores = {
        domain: weights.get(domain, 1.0) * (count**alpha) if count > 0 else 0.0
        for domain, count in domain_counts.items()
    }
    total = sum(scores.values())
    if total == 0:
        raise ValueError("Ningún dominio tiene documentos: no se puede muestrear")
    return {domain: score / total for domain, score in scores.items()}
