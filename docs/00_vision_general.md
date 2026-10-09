# Visión General — LLM Lab (Etapa 1)

## Filosofía

Este laboratorio sigue tres principios:

1. **Desde cero antes que con librerías.** Cada componente (tokenizador BPE, self-attention, loop de entrenamiento, LoRA) se implementa primero en NumPy/PyTorch puro, con shapes anotados y matemática derivada, y *después* se compara con la implementación de HuggingFace. Entender → verificar → usar.

2. **Visualizar todo lo interno.** Un LLM no es una caja negra si se inspecciona: attention maps, distribución de pesos por capa, norma de gradientes durante backprop, trayectoria de embeddings durante el entrenamiento, uso de VRAM por componente. Si no se puede graficar, no se entendió.

3. **Rigor industrial en un entorno educativo.** Seeds, configs declarativos, logging estructurado, checkpoints completos, perfiles de hardware. Las prácticas de un equipo de research real, a escala de una sola GPU, todo dentro de Docker.

## Alcance — Etapa 1 (este repo)

| Incluido | Excluido (Etapa 2) |
|----------|--------------------|
| Datasets y construcción de corpus | Agentes y sistemas multiagente |
| Tokenización (BPE, WordPiece, SentencePiece, Unigram) | RAG |
| Embeddings (estáticos y contextuales) | Serving y APIs de producción |
| Transformer decoder-only desde cero | Deployment / MLOps |
| Pre-entrenamiento (next-token prediction) | Observabilidad de producción |
| Fine-tuning (SFT, LoRA, QLoRA) | Tool calling / memoria |
| Evaluación (perplexity, BLEU, ROUGE, BERTScore, bias) | Workflows autónomos |
| Interpretabilidad y visualización interna | |

## El modelo objetivo

Un **decoder-only transformer estilo GPT** (la familia de GPT-2/3, Llama, Qwen, Mistral) con RoPE,
RMSNorm, SwiGLU y atención fusionada (SDPA), entrenado con next-token prediction y luego ajustado con
SFT. Hay dos juegos de tamaños, porque hay dos productos (ver [06 · Guía de ejecución](06_guia_ejecucion.md)):

**Pipeline de entrenamiento** (`scripts/` + `configs/`): el modelo que de verdad entrenas.

| | `tiny` | `small` | `large` |
|---|---|---|---|
| Hardware | CPU (contenedor en el Mac) | T4 16 GB | A100 / L4 / RTX 4090 |
| Parámetros | ~0.9 M | ~17 M | ~101 M |
| `d_model` · capas · heads | 128 · 2 · 4 | 384 · 6 · 6 | 768 · 12 · 12 (4 KV, GQA) |
| Contexto | 128 | 512 | 1024 |
| Vocabulario | 4 096 | 16 384 | 32 768 |
| Tokens de entrenamiento | ~1 M (smoke test) | ~350 M | ~2 B |
| Precisión | fp32 | fp16 | bf16 |

**Notebooks educativos 00–08**: cada uno define perfiles didácticos propios, más pequeños o con menos
pasos (SMALL ~5 M / LARGE ~110 M parámetros (≈85 M sin embeddings)), con datos de demostración.

## Dominios del corpus (26)

**Prioritarios (peso 1.5):** Estadística · Optimización · Metaheurísticas · Ciencia de Datos · Analítica y BI ·
Inteligencia Artificial · LLMs · Desarrollo Full Stack · Filosofía · Música.
**Fundamentos (1.2):** Machine Learning · Deep Learning · Matemáticas · Python.
**Resto (1.0):** Programación · PostgreSQL · MongoDB · AWS · Serverless · IaC · APIs · Arquitectura de Software ·
DevOps · Data Engineering · Sistemas Distribuidos · Ingeniería Eléctrica.

Pesos en [`configs/corpus.yaml`](../configs/corpus.yaml), léxico de cada dominio en
[`configs/domains.yaml`](../configs/domains.yaml) y mezcla de fuentes en [`configs/data.yaml`](../configs/data.yaml).

## Convenciones

- **Idioma:** prosa, explicaciones y comentarios en **español**; identificadores de código en **inglés**.
- **Notación matemática:** vectores en minúscula negrita ($\mathbf{x}$), matrices en mayúscula ($W$), shapes anotados como comentario en cada operación de tensores: `# (B, T, d_model)`.
- **B, T, C:** batch size, longitud de secuencia (time), canales/dimensión del modelo — la convención de Karpathy, usada en todo el repo.
