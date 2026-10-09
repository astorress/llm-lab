# Bibliografía — Deep Learning

> Dominio `deep_learning` · peso 1.2 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Deep Learning | I. Goodfellow, Y. Bengio, A. Courville | 2016 | 4 | 5 | Alta | 5 | 5 |
| F2 | Dive into Deep Learning (d2l.ai) | A. Zhang, Z. Lipton, M. Li, A. Smola | 2023 | 3 | 5 | Alta | 5 | 4 |
| F3 | Understanding Deep Learning | S. J. D. Prince | 2023 | 3 | 5 | Alta | 5 | 4 |

#### F1 — *Deep Learning* (Goodfellow et al.)
- **Cobertura conceptual:** fundamentos completos: backprop, regularización, optimización, CNN, RNN, autoencoders, modelos generativos.
- **Cobertura práctica:** entender por qué funcionan las técnicas; base teórica para leer cualquier paper posterior.
- **Valor como guía para el LLM:** el texto canónico del campo; su notación es la *lingua franca* que el modelo debe dominar.
- **Conocimiento que aporta:** la teoría pre-transformer que explica todos los componentes que este repo implementa desde cero.
- **Vocabulario técnico:** *backpropagation*, *vanishing gradient*, *weight decay*, *dropout*, *softmax*, *cross-entropy*, *embedding*.
- **Razonamiento que aporta:** derivación de gradientes, análisis de capacidad/regularización, justificación de elecciones arquitectónicas.

#### F2 — *Dive into Deep Learning*
- **Cobertura conceptual:** desde regresión lineal hasta transformers y attention, todo con código ejecutable (PyTorch/JAX/MXNet).
- **Cobertura práctica:** implementar cada arquitectura desde cero — exactamente la filosofía de este laboratorio.
- **Valor como guía para el LLM:** alterna matemática, código con shapes anotados y texto explicativo — el estilo de documento que se prioriza al filtrar el corpus.
- **Conocimiento que aporta:** la versión "ejecutable" de F1, incluyendo attention y transformers que F1 no cubre.
- **Vocabulario técnico:** *attention*, *multi-head*, *positional encoding*, *minibatch SGD*, *layer norm*, *BLEU*.
- **Razonamiento que aporta:** traducción matemática → código, debugging de shapes, ablaciones experimentales.

#### F3 — *Understanding Deep Learning*
- **Cobertura conceptual:** DL moderno post-transformer: transformers, difusión, RL, ética, con figuras excepcionales.
- **Cobertura práctica:** notebooks oficiales por capítulo; intuición visual de cada mecanismo.
- **Valor como guía para el LLM:** texto 2023 con terminología actual (LLMs, fine-tuning, RLHF) escrita con rigor de libro.
- **Conocimiento que aporta:** el puente entre los fundamentos (F1) y la práctica actual de LLMs.
- **Vocabulario técnico:** *residual stream*, *diffusion model*, *fine-tuning*, *RLHF*, *inductive bias*, *double descent*.
- **Razonamiento que aporta:** intuiciones geométricas, razonamiento sobre generalización moderna (double descent, lottery tickets).

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Deep Learning: Foundations and Concepts | C. M. Bishop, H. Bishop | 2024 | 4 | 5 | Alta | 5 | 5 |
| A2 | Probabilistic Machine Learning: Advanced Topics | K. P. Murphy | 2023 | 5 | 4 | Media | 5 | 5 |
| A3 | The Principles of Deep Learning Theory | D. A. Roberts, S. Yaida | 2022 | 5 | 3 | Baja | 4 | 5 |

#### A1 — *Deep Learning: Foundations and Concepts*
- **Cobertura conceptual:** reescritura moderna de PRML centrada en DL: transformers, GNN, difusión, con rigor probabilístico.
- **Cobertura práctica:** base sólida para diseñar y justificar arquitecturas modernas.
- **Valor como guía para el LLM:** rigor bayesiano aplicado a arquitecturas 2024 — combina rigor probabilístico y arquitecturas modernas.
- **Conocimiento que aporta:** tratamiento matemático formal de los transformers que el repo implementa.
- **Vocabulario técnico:** *autoregressive model*, *latent diffusion*, *score function*, *attention head*, *KV cache* (conceptos).
- **Razonamiento que aporta:** derivaciones probabilísticas de objetivos modernos (difusión, autoregresión).

#### A2 — *Probabilistic ML: Advanced Topics*
- **Cobertura conceptual:** inferencia variacional avanzada, modelos generativos profundos, procesos gaussianos, causalidad.
- **Cobertura práctica:** referencia enciclopédica para temas de investigación.
- **Valor como guía para el LLM:** cobertura de cola larga (temas raros) que amplía la cobertura del nivel avanzado.
- **Conocimiento que aporta:** el nivel `avanzado` del esquema de dificultad para este dominio.
- **Vocabulario técnico:** *normalizing flows*, *score-based models*, *amortized inference*, *SSM*, *neural ODE*.
- **Razonamiento que aporta:** unificación de familias generativas bajo un marco probabilístico común.

#### A3 — *The Principles of Deep Learning Theory*
- **Cobertura conceptual:** teoría de redes anchas con herramientas de física teórica (expansiones perturbativas, kernels NTK).
- **Cobertura práctica:** entender inicialización y propagación de señal — relevante para los experimentos de visualización interna del repo.
- **Valor como guía para el LLM:** registro de física-matemática aplicada a DL, poco común en otras fuentes.
- **Conocimiento que aporta:** por qué la inicialización y la profundidad importan, con derivaciones exactas.
- **Vocabulario técnico:** *neural tangent kernel*, *criticality*, *effective theory*, *signal propagation*, *width expansion*.
- **Razonamiento que aporta:** razonamiento perturbativo y de límites asintóticos, raro y valioso.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | Deep Learning with Python (2ª ed.) | F. Chollet | 2021 | 2 | 4 | Alta | 5 | 2 |
| P2 | Deep Learning for Coders with fastai and PyTorch | J. Howard, S. Gugger | 2020 | 2 | 4 | Media | 4 | 2 |
| P3 | Deep Learning with PyTorch | E. Stevens, L. Antiga, T. Viehmann | 2020 | 3 | 5 | Alta | 4 | 3 |

#### P1 — *Deep Learning with Python*
- **Cobertura conceptual:** workflow Keras completo, intuiciones de alto nivel del creador de Keras, capítulo final conceptual brillante.
- **Cobertura práctica:** construir y entrenar modelos de visión, texto y series temporales.
- **Valor como guía para el LLM:** prosa pedagógica excepcional — el "tono explicativo" que queremos que el modelo imite.
- **Conocimiento que aporta:** el mapa mental del practicante (qué arquitectura para qué problema).
- **Vocabulario técnico:** *functional API*, *callback*, *data augmentation*, *transfer learning*, *overfit deliberadamente primero*.
- **Razonamiento que aporta:** heurísticas de práctica (universal workflow of ML), diagnóstico de entrenamiento.

#### P2 — *Deep Learning for Coders (fastai)*
- **Cobertura conceptual:** enfoque top-down: aplicación primero, teoría después; visión, NLP, tabular, collaborative filtering.
- **Cobertura práctica:** resultados de estado del arte con pocas líneas; técnicas de entrenamiento (one-cycle, discriminative LR).
- **Valor como guía para el LLM:** registro conversacional con código — estilo distinto al académico.
- **Conocimiento que aporta:** trucos de entrenamiento empíricos documentados en pocos lugares.
- **Vocabulario técnico:** *learning rate finder*, *one-cycle policy*, *progressive resizing*, *discriminative learning rates*.
- **Razonamiento que aporta:** experimentación iterativa y debugging empírico de entrenamiento.

#### P3 — *Deep Learning with PyTorch*
- **Cobertura conceptual:** tensores, autograd, `nn.Module`, entrenamiento, despliegue; proyecto médico completo.
- **Cobertura práctica:** dominar PyTorch idiomático — la librería de este repo.
- **Valor como guía para el LLM:** la mejor fuente de PyTorch puro explicado línea a línea, directamente alineada con el código del laboratorio.
- **Conocimiento que aporta:** mecánica interna de autograd y el ciclo de entrenamiento que el repo implementa a mano.
- **Vocabulario técnico:** *autograd*, *computational graph*, *DataLoader*, *state_dict*, *device*, *in-place op*.
- **Razonamiento que aporta:** debugging de gradientes y memoria; diseño de loops de entrenamiento robustos.

## Papers importantes

- Vaswani, A. et al. — *Attention Is All You Need* (NeurIPS 2017). [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)
- He, K. et al. — *Deep Residual Learning for Image Recognition* (CVPR 2016). [arXiv:1512.03385](https://arxiv.org/abs/1512.03385)
- Kingma, D. & Ba, J. — *Adam: A Method for Stochastic Optimization* (ICLR 2015). [arXiv:1412.6980](https://arxiv.org/abs/1412.6980)
- Ioffe, S. & Szegedy, C. — *Batch Normalization* (ICML 2015). [arXiv:1502.03167](https://arxiv.org/abs/1502.03167)
- Devlin, J. et al. — *BERT: Pre-training of Deep Bidirectional Transformers* (NAACL 2019). [arXiv:1810.04805](https://arxiv.org/abs/1810.04805)
- Brown, T. et al. — *Language Models are Few-Shot Learners* (GPT-3, NeurIPS 2020). [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- Kaplan, J. et al. — *Scaling Laws for Neural Language Models* (2020). [arXiv:2001.08361](https://arxiv.org/abs/2001.08361)
- Hu, E. et al. — *LoRA: Low-Rank Adaptation of Large Language Models* (2021). [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)

## Documentación oficial

- [PyTorch docs + tutorials](https://pytorch.org/docs/) — BSD-3.
- [Hugging Face docs (transformers, datasets, tokenizers)](https://huggingface.co/docs) — Apache-2.0.
- [JAX docs](https://jax.readthedocs.io/) — Apache-2.0.

## Blogs técnicos

- [Andrej Karpathy](https://karpathy.github.io/) — incl. *A Recipe for Training Neural Networks*; sus videos/repos inspiran este repo.
- [Lilian Weng — Lil'Log](https://lilianweng.github.io/) — surveys profundos (attention, RLHF, diffusion).
- [colah.github.io](https://colah.github.io/) — intuiciones visuales clásicas (LSTM, backprop).
- [Distill.pub](https://distill.pub/) — interpretabilidad y visualización.
- [Sebastian Ruder](https://www.ruder.io/) — NLP y optimización (resumen clásico de optimizadores).

## Repositorios GitHub

- [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) y [karpathy/build-nanogpt](https://github.com/karpathy/build-nanogpt) — referencia directa del modelo objetivo de este repo.
- [d2l-ai/d2l-en](https://github.com/d2l-ai/d2l-en) — libro F2 completo (CC BY-SA).
- [huggingface/transformers](https://github.com/huggingface/transformers) — implementaciones de referencia.
- [labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations) — papers implementados y anotados.
- [pytorch/pytorch](https://github.com/pytorch/pytorch) — para leer kernels y autograd.

## Benchmarks

- **MMLU**, **HellaSwag**, **ARC**, **WinoGrande** — evaluación estándar de LMs (relevantes para evaluar el LLM de este repo).
- **GLUE / SuperGLUE** — NLU clásico.
- **ImageNet / CIFAR** — visión, útiles como referencia histórica.
- **Perplexity sobre WikiText-103 / The Pile** — el benchmark directo aplicable al modelo SMALL/LARGE del repo.

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

| Dataset | Licencia | Notas |
|---------|----------|-------|
| The Pile (EleutherAI) | MIT (código); contenidos mixtos — verificar por subset | 825 GB; subsets útiles: arXiv, StackExchange |
| FineWeb / FineWeb-Edu (HF) | ODC-By 1.0 | Web filtrada de alta calidad; FineWeb-2 incluye español |
| C4 | ODC-By | Corpus de T5 |
| OpenWebText | Dominio público declarado — verificar | Réplica del corpus de GPT-2 |
| WikiText-103 | CC BY-SA 3.0 | Benchmark clásico de perplexity |
