"""Esquema canónico de documentos del corpus (Fase 3).

Construcción y validación de documentos según
``datasets/schemas/document.schema.json``. El ``id`` es determinista:
sha256 del contenido normalizado, así el mismo texto produce siempre el
mismo documento (idempotencia del pipeline y dedup gratis).

``validate_document`` usa ``jsonschema`` con import perezoso: el paquete
``data`` debe ser importable sin esa dependencia instalada.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from llm_lab.data.chunking import approx_token_count
from llm_lab.data.cleaning import normalize_text, quality_score
from llm_lab.data.dedup import sha256_hash

__all__ = ["SCHEMA_PATH", "load_schema", "make_document", "validate_document"]

# Raíz del repo: src/llm_lab/data/schema.py -> tres niveles arriba.
_REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = _REPO_ROOT / "datasets" / "schemas" / "document.schema.json"


def load_schema(path: str | Path | None = None) -> dict[str, Any]:
    """Carga el JSON Schema canónico del documento."""
    schema_path = Path(path) if path else SCHEMA_PATH
    with schema_path.open(encoding="utf-8") as f:
        return json.load(f)


def make_document(
    content: str,
    domain: str,
    source: str,
    *,
    title: str | None = None,
    subcategory: str | None = None,
    difficulty: str | None = None,
    authors: list[str] | None = None,
    year: int | None = None,
    summary: str | None = None,
    metadata: dict[str, Any] | None = None,
    normalize: bool = True,
    tokens: int | None = None,
    score: float | None = None,
) -> dict[str, Any]:
    """Construye un documento del esquema canónico con id determinista.

    El id es ``sha256:<hash del contenido normalizado>``: dos llamadas con
    el mismo texto producen el mismo id, lo que hace el pipeline
    idempotente y permite dedup exacto comparando ids.

    Args:
        content: texto del documento (se normaliza salvo ``normalize=False``).
        domain: uno de los 26 dominios de configs/corpus.yaml.
        source: "libro" | "paper" | "documentacion" | "blog" | "codigo" | "sintetico".
        title, subcategory, difficulty, authors, year, summary: campos
            opcionales del esquema.
        metadata: dict opcional (language, license, url, chunk_index, ...).
        normalize: aplicar :func:`normalize_text` antes de hashear.
        tokens: conteo de tokens; si None se estima con
            :func:`approx_token_count`.
        score: quality_score precalculado; si None se calcula con
            :func:`quality_score`.

    Returns:
        Dict listo para serializar a JSONL y validar contra el schema.
    """
    text = normalize_text(content) if normalize else content
    if not text:
        raise ValueError("El contenido del documento no puede estar vacío")

    doc: dict[str, Any] = {
        "id": f"sha256:{sha256_hash(text)}",
        "domain": domain,
        "source": source,
        "quality_score": quality_score(text) if score is None else score,
        "tokens": approx_token_count(text) if tokens is None else tokens,
        "content": text,
    }
    # Campos opcionales: solo se incluyen si tienen valor (el schema usa
    # additionalProperties: false, pero los opcionales ausentes son válidos).
    optional = {
        "title": title,
        "subcategory": subcategory,
        "difficulty": difficulty,
        "authors": authors,
        "year": year,
        "summary": summary,
        "metadata": metadata,
    }
    doc.update({k: v for k, v in optional.items() if v is not None})
    return doc


def validate_document(
    doc: dict[str, Any],
    schema: dict[str, Any] | None = None,
    raise_on_error: bool = True,
) -> list[str]:
    """Valida un documento contra el JSON Schema canónico.

    Requiere el paquete ``jsonschema`` (import perezoso: solo se necesita
    al validar, no al importar este módulo).

    Args:
        doc: documento a validar.
        schema: schema alternativo; si None carga el canónico del repo.
        raise_on_error: si True lanza ValueError con los errores; si False
            devuelve la lista de mensajes (vacía = válido).

    Returns:
        Lista de mensajes de error (vacía si el documento es válido).
    """
    try:
        import jsonschema
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "validate_document requiere 'jsonschema': pip install jsonschema"
        ) from exc

    schema = schema or load_schema()
    validator = jsonschema.Draft202012Validator(schema)
    errors = [
        f"{'/'.join(str(p) for p in error.absolute_path) or '<root>'}: {error.message}"
        for error in validator.iter_errors(doc)
    ]
    if errors and raise_on_error:
        raise ValueError("Documento inválido:\n- " + "\n- ".join(errors))
    return errors
