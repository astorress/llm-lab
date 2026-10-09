"""Limpieza y filtrado de calidad del corpus (Fase 3).

Implementa heurísticas de calidad inspiradas en el pipeline de Gopher
(Rae et al., 2021, "Scaling Language Models: Methods, Analysis & Insights
from Training Gopher", apéndice A): longitud del documento, proporción de
caracteres alfabéticos, proporción de símbolos y líneas repetidas.

La idea central: cada heurística devuelve un sub-score en [0, 1] y el
``quality_score`` final es el promedio ponderado — componible y fácil de
inspeccionar (se puede graficar la distribución de cada sub-score por
dominio antes de fijar el umbral ``quality.min_quality_score``).
"""

from __future__ import annotations

import unicodedata
from dataclasses import dataclass, field

__all__ = [
    "normalize_text",
    "char_length_score",
    "alpha_ratio",
    "symbol_ratio",
    "repeated_lines_ratio",
    "QualityConfig",
    "quality_score",
]

# Símbolos típicos de texto "basura" (boilerplate, tablas rotas, OCR malo).
_SYMBOLS = set("#@*+=|~^<>{}[]\\")


def normalize_text(text: str) -> str:
    """Normaliza un texto: Unicode NFKC + espacios colapsados.

    - NFKC unifica formas de compatibilidad (ligaduras, anchos completos,
      espacios raros como U+00A0) para que el dedup exacto por hash no se
      rompa por diferencias invisibles.
    - Colapsa espacios/tabs múltiples dentro de cada línea y elimina
      líneas vacías repetidas (máximo una línea en blanco seguida).

    Args:
        text: texto crudo.

    Returns:
        Texto normalizado, sin espacios al inicio/fin.
    """
    text = unicodedata.normalize("NFKC", text)
    lines: list[str] = []
    blank_run = 0
    for raw_line in text.splitlines():
        line = " ".join(raw_line.split())  # colapsa espacios internos
        if line:
            blank_run = 0
            lines.append(line)
        else:
            blank_run += 1
            if blank_run == 1:
                lines.append("")
    return "\n".join(lines).strip()


def char_length_score(text: str, min_chars: int = 200, max_chars: int = 500_000) -> float:
    """Sub-score por longitud: 1.0 dentro del rango, 0.0 fuera.

    Documentos muy cortos suelen ser fragmentos sin contexto; los muy
    largos suelen ser dumps/concatenaciones (mejor trocearlos antes).
    """
    n = len(text)
    return 1.0 if min_chars <= n <= max_chars else 0.0


def alpha_ratio(text: str) -> float:
    """Proporción de caracteres alfabéticos sobre caracteres no-espacio.

    Texto técnico legítimo (incluso con código) mantiene un alpha_ratio
    alto; tablas rotas, ASCII art o dumps numéricos lo hunden.
    """
    chars = [c for c in text if not c.isspace()]
    if not chars:
        return 0.0
    return sum(c.isalpha() for c in chars) / len(chars)


def symbol_ratio(text: str) -> float:
    """Proporción de símbolos 'sospechosos' sobre caracteres no-espacio.

    Gopher usa #/... como señal de boilerplate; aquí ampliamos el set a
    símbolos comunes en markup roto y OCR defectuoso.
    """
    chars = [c for c in text if not c.isspace()]
    if not chars:
        return 0.0
    return sum(c in _SYMBOLS for c in chars) / len(chars)


def repeated_lines_ratio(text: str) -> float:
    """Fracción de líneas duplicadas (no vacías) sobre el total de líneas.

    Un valor alto delata headers/footers repetidos, menús de navegación
    o plantillas — contenido de bajo valor para el modelo.
    """
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return 0.0
    return 1.0 - len(set(lines)) / len(lines)


@dataclass
class QualityConfig:
    """Umbrales del filtro de calidad (defaults de configs/corpus.yaml)."""

    min_chars: int = 200
    max_chars: int = 500_000
    min_alpha_ratio: float = 0.6
    max_symbol_ratio: float = 0.15
    max_repeated_lines: float = 0.30
    # Peso de cada heurística en el promedio final (se normalizan).
    weights: dict[str, float] = field(
        default_factory=lambda: {
            "length": 1.0,
            "alpha": 1.0,
            "symbol": 1.0,
            "repeated": 1.0,
        }
    )


def quality_score(text: str, config: QualityConfig | None = None) -> float:
    """Calcula un score de calidad componible en [0, 1] estilo Gopher.

    Cada heurística aporta un sub-score:
    - length: binario (dentro/fuera del rango de caracteres).
    - alpha: rampa lineal 0→1 hasta ``min_alpha_ratio`` (1.0 si lo supera).
    - symbol: rampa inversa — 1.0 si symbol_ratio=0, 0.0 si llega al doble
      de ``max_symbol_ratio``.
    - repeated: rampa inversa análoga sobre líneas repetidas.

    El score final es el promedio ponderado de los sub-scores. Para un
    filtro duro tradicional, comparar contra ``quality.min_quality_score``.

    Args:
        text: texto YA normalizado (ver :func:`normalize_text`).
        config: umbrales; si None usa los defaults del corpus.

    Returns:
        Score en [0, 1]; 1.0 = pasa todas las heurísticas con holgura.
    """
    cfg = config or QualityConfig()

    s_length = char_length_score(text, cfg.min_chars, cfg.max_chars)

    a = alpha_ratio(text)
    s_alpha = min(1.0, a / cfg.min_alpha_ratio) if cfg.min_alpha_ratio > 0 else 1.0

    s = symbol_ratio(text)
    s_symbol = max(0.0, 1.0 - s / (2 * cfg.max_symbol_ratio)) if cfg.max_symbol_ratio > 0 else 1.0

    r = repeated_lines_ratio(text)
    s_repeated = max(0.0, 1.0 - r / (2 * cfg.max_repeated_lines)) if cfg.max_repeated_lines > 0 else 1.0

    subscores = {
        "length": s_length,
        "alpha": s_alpha,
        "symbol": s_symbol,
        "repeated": s_repeated,
    }
    total_weight = sum(cfg.weights.get(k, 0.0) for k in subscores)
    if total_weight == 0:
        return 0.0
    score = sum(subscores[k] * cfg.weights.get(k, 0.0) for k in subscores) / total_weight
    return round(score, 4)
