"""Clasificador léxico de dominio (Fase 3 — filtrado del corpus de pre-entrenamiento).

Idea: un documento es "de dominio" si menciona varios términos DISTINTOS del
léxico de ``configs/domains.yaml``. Contar términos distintos (no ocurrencias)
evita que un texto que repite "voltaje" 40 veces pase como técnico.

    hits_d(doc)  = |{t ∈ léxico_d : t aparece en doc}|
    total(doc)   = Σ_d hits_d(doc)          → filtro: total ≥ min_domain_hits
    dominio(doc) = argmax_d hits_d(doc)     → etiqueta para balanceo y métricas

Es el mismo principio que los filtros heurísticos de FineWeb/Gopher: barato
(una regex por dominio), explicable y fácil de auditar mirando qué términos
dispararon. Un clasificador neuronal de calidad sería la evolución natural.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

__all__ = ["DomainClassifier", "DomainMatch"]

_DEFAULT_LEXICON = Path(__file__).resolve().parents[3] / "configs" / "domains.yaml"


@dataclass
class DomainMatch:
    domain: str | None        # dominio con más términos distintos (None si 0)
    total_hits: int           # términos distintos sumados sobre todos los dominios
    hits: dict[str, int]      # términos distintos por dominio


class DomainClassifier:
    """Cuenta términos distintos del léxico por dominio.

    Args:
        lexicon_path: YAML {dominio: [términos]}; default ``configs/domains.yaml``.
        max_chars: solo se inspeccionan los primeros ``max_chars`` caracteres
            (el tema de un documento se decide en su inicio y así el costo es O(1)).
    """

    def __init__(self, lexicon_path: str | Path | None = None, max_chars: int = 6000):
        path = Path(lexicon_path) if lexicon_path else _DEFAULT_LEXICON
        with path.open(encoding="utf-8") as f:
            lexicon: dict[str, list[str]] = yaml.safe_load(f)
        self.max_chars = max_chars
        self.domains = list(lexicon)
        # Una regex por dominio con alternancia; los términos largos primero para
        # que "aprendizaje automático" gane sobre prefijos más cortos.
        self._patterns: dict[str, re.Pattern] = {}
        for domain, terms in lexicon.items():
            alts = sorted({t.lower() for t in terms}, key=len, reverse=True)
            body = "|".join(re.escape(t) for t in alts)
            self._patterns[domain] = re.compile(rf"(?<!\w)(?:{body})(?!\w)")

    def classify(self, text: str) -> DomainMatch:
        sample = text[: self.max_chars].lower()
        hits = {d: len(set(p.findall(sample))) for d, p in self._patterns.items()}
        total = sum(hits.values())
        best = max(hits, key=hits.get) if total > 0 else None
        return DomainMatch(domain=best, total_hits=total, hits=hits)

    def matched_terms(self, text: str, domain: str) -> set[str]:
        """Términos concretos que dispararon un dominio (para auditar el filtro)."""
        return set(self._patterns[domain].findall(text[: self.max_chars].lower()))
