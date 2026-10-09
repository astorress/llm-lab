# Esquema del Corpus

El proyecto maneja **dos formatos de corpus**:

| Corpus | Lo produce | Formato | Uso |
|---|---|---|---|
| **Semilla** (55 docs curados) | `scripts/build_corpus.py` | JSONL con el esquema canónico de abajo + Parquet | fuente local del pipeline (`seed`) |
| **Pre-entrenamiento** (por perfil) | `scripts/build_pretrain_corpus.py` | `datasets/pretrain/<perfil>/<fuente>.jsonl.gz` con `{text, domain, source, lang}` | entrada del tokenizador y de `tokenize_corpus.py` |
| **Tokenizado** | `scripts/tokenize_corpus.py` | `datasets/tokenized/<perfil>/train_<fuente>.bin` (uint16) + `val.bin` + `meta.json` | lo que lee el entrenamiento (memmap) |


## Formatos y cuándo usar cada uno

| Formato | Uso en el proyecto | Por qué |
|---------|--------------------|---------|
| **JSONL** | Formato canónico de intercambio (`datasets/processed/*.jsonl`) | Legible, streameable línea a línea, soportado nativamente por `datasets.load_dataset("json", ...)`. Un documento = una línea. |
| **Parquet** | Almacenamiento analítico (`datasets/processed/*.parquet`) | Columnar + comprimido (~5-10× menor que JSONL), filtros por columna sin cargar todo (p. ej. `domain == "metaheuristica"`). |
| **Arrow** | Formato interno de HF `datasets` (cache) | Memory-mapped: permite iterar corpus mayores que la RAM. Se genera automáticamente, no se versiona. |
| **Markdown** | Corpus semilla crudo (`datasets/raw/seed/*.md`) | Lo escribe `build_corpus.py` desde `scripts/seed_documents.py` para poder leerlo. |
| **gzip JSONL** | Corpus de pre-entrenamiento por fuente | Compacto y streameable; un documento por línea. |
| **`.bin` (memmap)** | Tokens listos para entrenar | Acceso aleatorio O(1) a ventanas de T tokens sin cargar nada en RAM. |

**Corpus semilla:** `seed_documents.py → raw/seed/*.md → JSONL canónico → Parquet`. **Pre-entrenamiento:** `fuentes (HF/local) → jsonl.gz por fuente → .bin por fuente`. Arrow solo aparece como caché interna de HF `datasets`.

## Esquema canónico del documento

Definido formalmente en [`datasets/schemas/document.schema.json`](../datasets/schemas/document.schema.json):

```json
{
  "id": "sha256:9f86d081...",
  "domain": "metaheuristica",
  "subcategory": "trayectoria_y_enjambre",
  "difficulty": "avanzado",
  "source": "libro|paper|documentacion|blog|codigo|sintetico",
  "quality_score": 0.87,
  "tokens": 1432,
  "title": "Recocido simulado y búsqueda tabú",
  "authors": ["E.-G. Talbi"],
  "year": 2009,
  "content": "...texto completo del documento o chunk...",
  "summary": "Criterio de aceptación de Metropolis y esquemas de enfriamiento...",
  "metadata": {
    "language": "es",
    "license": "...",
    "url": "...",
    "chunk_index": 3,
    "chunk_total": 12,
    "parent_id": "sha256:...",
    "has_math": true,
    "has_code": false,
    "extraction_method": "markdown_parser",
    "dedup_cluster": null
  }
}
```

### Campos

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | `sha256:` + hash del contenido normalizado. Determinista: re-procesar produce el mismo id (clave para dedup). |
| `domain` | enum | Uno de los 26 dominios de `configs/corpus.yaml`. |
| `subcategory` | string | Subtema libre dentro del dominio (p. ej. `evolutivos`, `lora`, `indices_btree`). |
| `difficulty` | enum | `introductorio` \| `intermedio` \| `avanzado` — metadato descriptivo (no se usa todavía para curriculum learning). |
| `source` | enum | Tipo de fuente; pondera la confianza del documento. |
| `quality_score` | float 0–1 | Heurísticas estilo Gopher (`llm_lab.data.cleaning`): longitud, ratio alfabético, ratio de símbolos y líneas repetidas. |
| `tokens` | int | Estimación por palabras (≈1.3 tokens/palabra, `approx_token_count`); el conteo exacto con el tokenizador propio queda en `datasets/tokenized/<perfil>/meta.json`. |
| `content` | string | El texto. Si el documento fue chunkeado, es el chunk; el original se referencia con `metadata.parent_id`. |
| `metadata.has_math/has_code` | bool | Marcas heurísticas para análisis (no se usan para muestrear). |

## Weighting de dominios

Hay dos mecanismos, en etapas distintas:

**1. Al construir el corpus de pre-entrenamiento** (`build_pretrain_corpus.py`, lo que de verdad afecta al
modelo). En cada fuente mixta con presupuesto:
- un documento del dominio *d* se acepta con probabilidad $w_d / \max_{d'} w_{d'}$ (pesos de
  `configs/corpus.yaml`: los dominios con peso 1.5 se aceptan siempre; los de 1.0, ~67 % de las veces);
- ningún dominio puede superar `max_domain_share` (30 %) de los tokens de la fuente.

**2. Al entrenar** (`TokenDataset`): cada batch elige la fuente con $p_s \propto \text{tokens}_s \cdot \text{repeat}_s$
(`repeat` en `configs/data.yaml`, re-ajustable con `pretrain.py --repeat personal=1`).

**3. Solo informativo, corpus semilla:** `build_corpus.py` escribe en `corpus_manifest.json` las probabilidades
$P(d) = \frac{w_d \cdot n_d^{\alpha}}{\sum_{d'} w_{d'} \cdot n_{d'}^{\alpha}}$ con $\alpha = 0.7$ (estilo XLM-R), que el
notebook 03 usa para explicar el sobre-muestreo de dominios pequeños.

## Splits

- **Corpus semilla:** `build_corpus.py` separa por defecto 10 % validación y 10 % test **por dominio**
  (con 2 documentos por dominio, el redondeo deja la mayoría en train: hoy 50/1/4). Deduplica antes del split
  y verifica que ningún documento de test tenga un near-duplicate en train.
- **Pre-entrenamiento:** `tokenize_corpus.py` envía el 0.5 % de los documentos (`val_fraction`, elegido por hash,
  determinista) a `val.bin`; los de tu corpus personal van además a `val_personal.bin`.
