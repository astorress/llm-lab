# 07 · Entrenamiento práctico: de tu corpus a tu modelo

Qué entrenas, con qué datos, dónde conviene hacerlo y cómo experimentar. Los **comandos paso a paso**
(contenedor, smoke test, datos, GPU con Docker, Colab/Kaggle) están en
[06 · Guía de ejecución](06_guia_ejecucion.md); aquí no se repiten.

## 1. Qué vas a entrenar

Un **MiniGPT decoder-only** (RoPE, RMSNorm, SwiGLU, SDPA/Flash, weight tying) pre-entrenado desde cero
sobre un corpus bilingüe orientado a tu perfil, y luego ajustado con SFT a formato de asistente.

| Perfil | Hardware | Parámetros | Tokens planificados | Tiempo (estimado, no medido) | Para qué sirve |
|---|---|---|---|---|---|
| `tiny`  | CPU, contenedor en el Mac | ~0.9 M | ~1 M (300 pasos) | minutos | validar el pipeline de punta a punta |
| `small` | T4 16 GB (Colab / Kaggle / host GPU) | ~17 M | ~350 M (5 300 pasos) | 1.5–2 h | primer modelo real del dominio |
| `large` | A100 / L4 / RTX 4090 | ~101 M | ~2 B (7 600 pasos) | 3–5 h | escala cercana a GPT-2 small |

Los tiempos salen de estimar el throughput (FLOPs ≈ 6·N por token y ~30–40 % de utilización de la GPU);
el valor real lo verás en la métrica `tokens_per_sec` del log.

Regla usada para dimensionar: **Chinchilla** (Hoffmann et al., 2022) — ~20 tokens por parámetro es el
punto compute-óptimo. Con el mismo cómputo, un modelo más grande con menos datos o uno más chico con más
datos rinden peor.

Expectativa honesta: un modelo de 17–100 M parámetros **no** razona como un asistente comercial. Aprende
vocabulario, estilo y hechos frecuentes de tus dominios. El valor del proyecto es entender y controlar
todo el pipeline, y tener una base para experimentos (ablaciones de datos, arquitectura, SFT).

## 2. El corpus: "todo lo que sé de ti"

`configs/data.yaml` define la mezcla. El modelo se especializa en tu perfil profesional por tres vías:

1. **Corpus personal** (`configs/personal.yaml` → `scripts/collect_personal_corpus.py`): tesis y artículo
   de **Mixture of Experts y series de tiempo** (LaTeX), notebooks y código de la maestría, libros propios en
   PDF, proyectos de MLflow/SageMaker/Scala y la bibliografía de este laboratorio. Cada documento se etiqueta
   por su contenido con el mismo léxico. Se repite **×4** (es lo que más queremos que aprenda), se
   redactan secretos y correos, y **nunca** se versiona.
2. **Filtro de dominio** (`configs/domains.yaml`): léxico bilingüe de 26 dominios. **Prioritarios (peso 1.5)**:
   estadística, optimización, metaheurísticas, ciencia de datos, analítica/BI, IA, LLMs, full stack, filosofía y
   música. Fundamentos (1.2): ML, DL, matemáticas, Python. Resto del stack (1.0): programación, PostgreSQL/MongoDB,
   AWS/Serverless/IaC, APIs, arquitectura, DevOps, data engineering, sistemas distribuidos, ing. eléctrica.
   Solo pasan documentos web con ≥4–5 términos distintos del léxico, y en las fuentes mixtas un doc se acepta con
   probabilidad w_d / max(w): los temas prioritarios ocupan más presupuesto.
3. **Fuentes públicas seleccionadas** (todas verificadas en el Hub de Hugging Face):

| Fuente | Idioma | % | Por qué |
|---|---|---|---|
| Wikipedia ES (filtrada) | es | 20 % | técnica + filosofía y música en español |
| FineWeb-2 `spa_Latn` (filtrada) | es | 17 % | español web técnico de calidad |
| FineWeb-Edu `sample-10BT` (score ≥3, filtrada) | en | 20 % | texto educativo de alta calidad |
| Cosmopedia v2 | en | 12 % | libros de texto sintéticos (ideal para modelos chicos) |
| Wikipedia EN (filtrada) | en | 8 % | cobertura enciclopédica (incl. humanidades) |
| OpenWebMath | en | 8 % | matemáticas con LaTeX |
| arXiv abstracts (stat.*, math.OC, cs.NE, cs.LG, cs.CL, cs.IR, cs.HC, cs.SD, physics.hist-ph…) | en | 7 % | estadística, optimización/metaheurísticas, ML/LLM, web, audio/música, filosofía de la ciencia |
| codeparrot-clean (Python) | code | 8 % | código Python |
| Personal ×4 + semilla ×8 | es | aparte | tu voz y tus temas |

Además, ningún dominio puede pasar del 30 % de una fuente mixta (`max_domain_share`), y la ponderación
final se aplica en el DataLoader (`p ∝ tokens · repeat`), así que puedes re-balancear sin re-tokenizar.

## 3. Ejecución

Ver [06 · Guía de ejecución](06_guia_ejecucion.md): §3 ruta Docker (Mac → host GPU) y §4 ruta Colab/Kaggle.

## 4. ¿Colab, Kaggle u otra cosa?

Condiciones y precios aproximados según lo conocido al escribir esto — cambian seguido, verifícalos antes de pagar.

| Opción | GPU | Costo | Límites | Veredicto |
|---|---|---|---|---|
| **Kaggle Notebooks** | T4 ×2 / P100 | **gratis**, ~30 h GPU/semana | sesión ≤ 12 h, corre en background con *Save Version*; el script usa 1 de las 2 T4 | **Mejor opción gratis para `small`** |
| Colab Free | T4 | gratis | sesiones cortas, sin garantía de GPU, se corta si cierras la pestaña | sirve, con checkpoints cada 250 pasos |
| Colab Pro | T4 / L4 / A100 | ~USD 10/mes (100 unidades; A100 ≈ 12 u/h) | unidades se agotan | `large` en A100 cabe en un mes (~3 h ≈ 36 u) |
| **RunPod / Vast.ai / VM con GPU** | RTX 4090 / A100 | ~USD 0.3–0.7/h (4090) · ~1.2–1.9/h (A100) | pagas por hora, sin cortes | **Mejor para `large`** con la imagen `img-gpu` (≈ USD 2–4 según el tiempo real) |
| Lightning AI Studios | T4 / L4 | créditos gratis mensuales | cuota limitada | alternativa a Colab con disco persistente |

**Recomendación**: datos en el contenedor del Mac (usa todos los núcleos, gratis) → `small` en **Kaggle**
(gratis, background) → si te gusta el resultado, `large` en un host GPU con la imagen Docker o en Colab Pro A100.
El Mac no sirve para entrenar `small`: Docker en macOS no tiene acceso a la GPU.
No uses la cuenta AWS de tu trabajo para este proyecto personal.

## 5. Buenas prácticas de entrenamiento

- **Siempre smoke test primero** (`make smoke`, luego en la GPU
  `python scripts/pretrain.py --profile small --max_steps 50 --out_dir checkpoints/small-prueba`).
  Un error al paso 4 000 cuesta horas.
- **Checkpoints fuera de la VM**: `--out_dir` en Drive / `/kaggle/working`. `last.pt` guarda optimizador,
  scheduler, GradScaler, RNG y estado del DataLoader → reanudar es exacto.
- **Datos en disco local**, no en Drive: el notebook extrae el `.tar` en la VM.
- **Mira tres curvas**: `val_loss` (generalización), `val_personal_loss` (cuánto aprende de *ti*) y
  `tokens_per_sec` (si cae, hay cuello de botella de datos o throttling).
- **Diagnóstico rápido de la loss**:
  - Empieza en ≈ ln(vocab) (9.7 para 16k). Si no, la inicialización está mal.
  - Diverge / NaN → baja `lr` ×0.5, revisa `grad_norm` (picos > 10), en fp16 sube `warmup_steps`.
  - `val_personal_loss` ≪ `val_loss` y sigue bajando mientras `val_loss` se estanca → sobreajuste al
    corpus personal: relanza con `--repeat personal=2` (o menos) en un `--out_dir` nuevo.
  - Train baja y val sube → más datos o menos pasos (con 1 época sobre datos únicos casi no ocurre).
- **Throughput**: `use_sdpa: true` siempre en GPU; `compile: true` en A100/4090 (suele acelerar, cuesta
  1–2 min de compilación al inicio); en T4 OOM →
  baja `batch_size` y sube `gradient_accumulation_steps` (el batch efectivo y la dinámica no cambian).
- **Reproducibilidad**: cada run guarda `model_config.json`, `tokenizer.json` y la config completa en el
  checkpoint. No edites `configs/` a mitad de un run reanudable.

## 6. Prácticas (experimentos guiados)

Todos los comandos van dentro del contenedor (o en la terminal del host GPU / celda `!` en Colab). Usa
**un `--out_dir` distinto por experimento** con `--fresh`; si no, el script reanuda el run anterior.

| # | Práctica | Comando | Qué observar |
|---|---|---|---|
| P1 | Smoke test | `make smoke` | que todo el pipeline termine; la loss baja desde ≈ 8.3 |
| P2 | Sobreajuste | `python scripts/pretrain.py --profile tiny --max_steps 3000 --fresh --out_dir checkpoints/tiny-overfit` | la train loss sigue bajando mientras `val_loss` se estanca o sube: memorización |
| P3 | Barrido de LR | `python scripts/pretrain.py --profile small --max_steps 300 --lr 3e-4 --fresh --out_dir checkpoints/lr3e-4` (repetir con `1e-3` y `3e-3`) | loss a los 300 pasos vs LR: la "U" del LR óptimo |
| P4 | Run completo `small` | notebook 09 o `make train PROFILE=small` en un host GPU | curvas completas; muestras de texto en cada evaluación |
| P5 | Peso del corpus personal | `... --profile small --repeat personal=1 --fresh --out_dir checkpoints/rep1` (y `=8`) | `val_personal_loss` vs `val_loss`: especialización vs generalidad |
| P6 | Ablación de arquitectura | edita temporalmente `configs/small.yaml` (`swiglu: false`, `n_kv_heads: 2`…) y corre con `--fresh --out_dir checkpoints/abl-…` | loss y tokens/s a igual cómputo (restaura el yaml al terminar) |
| P7 | SFT | `make sft chat PROFILE=small` | el modelo adopta el formato pregunta→respuesta |
| P8 | Escalado | `large` en A100/4090 | loss final vs `small`: ley de escalado empírica |

## 7. Siguiente nivel

- **Más SFT**: amplía `datasets/sft` (hoy 48 ejemplos) con preguntas sobre tus propios documentos. Para
  que el modelo responda de forma útil hacen falta cientos o miles de ejemplos, no decenas.
- **Ruta híbrida** (cuando quieras calidad de asistente): LoRA/QLoRA sobre un modelo abierto
  (SmolLM2 / Qwen2.5, ver notebook 07) usando **el mismo corpus personal y SFT** de este pipeline.
- **Clasificador de calidad neuronal** en lugar del filtro léxico (estilo FineWeb-Edu).
- **Evaluación por dominio** (pendiente): hoy solo hay `val_loss` global y `val_personal_loss`; separar `val.bin` por dominio permitiría perplexity por tema.
