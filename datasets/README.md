# Datasets — Corpus del LLM Lab

Formato y campos: [`docs/04_esquema_corpus.md`](../docs/04_esquema_corpus.md). Cómo ejecutar cada paso:
[`docs/06_guia_ejecucion.md`](../docs/06_guia_ejecucion.md) (todos los comandos van dentro del contenedor `LLMLab`).

## Estructura

```
datasets/
├── schemas/document.schema.json   # JSON Schema del documento del corpus semilla (versionado)
├── raw/
│   ├── seed/<dominio>.md          # corpus semilla en Markdown, 26 archivos (versionado)
│   └── personal/personal.jsonl    # TU corpus personal (make personal) — NUNCA se versiona
├── processed/                     # corpus semilla procesado (make seed)
│   ├── corpus.jsonl · corpus.parquet · corpus_manifest.json
├── splits/{train,val,test}.jsonl  # splits del corpus semilla
├── sft/                           # dataset de instruction tuning (versionado, curado)
│   ├── instructions.jsonl · train.jsonl · val.jsonl
├── pretrain/<perfil>/             # corpus de pre-entrenamiento filtrado (make corpus) — no versionado
│   ├── <fuente>.jsonl.gz · <fuente>.done · manifest.json
└── tokenized/<perfil>/            # tokens listos para entrenar (make tokenize) — no versionado
    ├── train_<fuente>.bin · val.bin · val_personal.bin · meta.json
```

## Estado actual del corpus semilla

| Métrica | Valor |
|---------|-------|
| Documentos | 55 |
| Dominios cubiertos | 26 / 26 |
| Tokens estimados | ~7 700 |
| Splits | train 50 · val 1 · test 4 |
| Ejemplos SFT | 48 (train 41 · val 7) |
| Validación de esquema | 55/55 ✓ |

El corpus semilla es pequeño a propósito: contenido técnico real escrito a mano para validar el pipeline y
aportar ejemplos limpios de cada dominio (en el pre-entrenamiento se repite ×8). El volumen real del
corpus (~350 M tokens en `small`) viene de las fuentes de `configs/data.yaml` y de tu corpus personal.

## Regenerar

```bash
make seed       # = python scripts/build_corpus.py && python scripts/build_sft.py
```

`build_corpus.py` usa el código de `llm_lab.data`: normalización, `quality_score`, dedup exacta y near-dup
(MinHash), chunking, id determinista, validación contra el JSON Schema y splits por dominio sin fuga
train/test. La fuente curada vive en `scripts/seed_documents.py` (documentos) y `scripts/build_sft.py`
(ejemplos SFT).

## Ampliar

1. **Más documentos semilla:** añade entradas en `scripts/seed_documents.py` (dominios válidos: los de
   `configs/corpus.yaml`; si agregas un dominio, actualiza también el `enum` del schema y `configs/domains.yaml`).
2. **Más SFT:** añade tuplas `(dominio, instrucción, respuesta)` en `scripts/build_sft.py`.
3. **Más fuentes de pre-entrenamiento:** añade una entrada en `configs/data.yaml` (tipo `hf` o `local_jsonl`)
   respetando su licencia.
