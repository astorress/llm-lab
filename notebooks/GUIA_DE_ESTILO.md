# Guía de Estilo de los Notebooks — LLM Lab

Contrato de los notebooks educativos 00–08. (El `09_entrenamiento_colab_kaggle` es un lanzador del pipeline y no sigue esta estructura.) Estilo objetivo: notebooks de curso de Stanford CS224N/CS324, Karpathy, HuggingFace Research.

## Estructura obligatoria de cada notebook

1. **Celda de título** (markdown): título, fase, objetivos de aprendizaje (lista), prerrequisitos, tiempo estimado SMALL/LARGE, badge "Open in Colab" (`colab.research.google.com/github/astorress/llm-lab/blob/main/notebooks/<nb>.ipynb`).
2. **Tabla de contenidos** (markdown con anchors).
3. **Celda de setup** (código): instala dependencias faltantes con `pip install -q` (sin reinstalar torch en Colab), detecta hardware (CUDA > MPS > CPU), detecta si corre en Colab, fija seeds (Python/NumPy/Torch/CUDA, `SEED = 42`), configura matplotlib/seaborn.
4. **Celda de configuración SMALL/LARGE** (código): `PROFILE = "auto"` (auto-detección por VRAM, forzable a mano) y un dict `CONFIG` con los hiperparámetros de ambos perfiles.
5. **Secciones numeradas**: cada sección = markdown profundo (teoría + matemática + intuición) seguido de código ejecutable + visualización.
6. **Sección final**: resumen, ejercicios propuestos (3–5, con dificultad), referencias (papers con enlaces arXiv, libros, blogs).

## Reglas de contenido

- **Idioma:** prosa y comentarios en español; identificadores de código en inglés.
- **Matemática:** LaTeX en markdown (`$...$` y `$$...$$`). Toda fórmula importante se acompaña de: (a) derivación o justificación, (b) ejemplo numérico pequeño verificable a mano, (c) implementación en código, (d) visualización.
- **Shapes:** todo tensor lleva su shape como comentario: `x = ...  # (B, T, d_model)`.
- **Convención B/T/C:** batch, tiempo (longitud de secuencia), canales (d_model).
- **Diagramas Mermaid:** en celdas markdown (se renderizan en GitHub; en Colab se incluye también descripción textual).
- **Desde cero primero:** implementar en NumPy/PyTorch puro → verificar contra la librería de referencia (HF, sklearn) → recién entonces usar la librería.
- **Verificaciones:** usar `assert` y `torch.allclose` para validar implementaciones propias contra referencias.
- **Sin descargas frágiles:** los datos de demo se generan sintéticamente o se incluyen inline; si se descarga algo (HF datasets/models) debe haber `try/except` con fallback y mensaje claro.
- **Autocontenido:** el notebook corre completo en Colab (o en el contenedor) sin el resto del repo. No importa `src/llm_lab`; ese paquete es la versión limpia que usa el pipeline de `scripts/`.

## Visualizaciones mínimas por notebook

Cada notebook incluye las que apliquen de: heatmaps (matplotlib/seaborn), visualización de tensores y matrices, attention maps, histogramas de activaciones y pesos, gradient flow por capa, distribución de tokens, learning curves (loss/accuracy/perplexity), proyecciones de embeddings (PCA/t-SNE/UMAP), monitoreo de GPU/VRAM, throughput (tokens/seg) y latencia. Plotly para los gráficos interactivos (3D, hover), matplotlib/seaborn para el resto.

## Formato técnico del archivo .ipynb

- `nbformat` 4.5: cada celda con `id` único, metadata de kernel python3.
- Celdas de código **sin outputs** guardados (`"outputs": [], "execution_count": null`).
- Markdown denso pero en celdas separadas por subsección (no muros de texto de >150 líneas por celda).
