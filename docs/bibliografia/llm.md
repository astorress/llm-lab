# Bibliografía — Modelos de Lenguaje Grandes (LLM)

> Dominio `llm` · peso 1.5 · [índice maestro](../02_libros_y_fuentes.md)

**Alcance:** Cómo se construyen, entrenan, alinean, evalúan y aplican los LLM: el tema central de este laboratorio.

## Libros

### Fundamentales

| Título | Autores | Año | Aporte al LLM |
|---|---|---|---|
| Build a Large Language Model (From Scratch) | S. Raschka | 2024 | GPT completo en PyTorch, paso a paso |
| Speech and Language Processing (3ª ed., borrador) | D. Jurafsky, J. H. Martin | 2024 | Gratis en línea; NLP y transformers con rigor |
| Natural Language Processing with Transformers | L. Tunstall, L. von Werra, T. Wolf | 2022 | Ecosistema Hugging Face |

### Avanzados

| Título | Autores | Año | Aporte al LLM |
|---|---|---|---|
| Hands-On Large Language Models | J. Alammar, M. Grootendorst | 2024 | Intuición visual de embeddings, atención y RAG |
| AI Engineering | C. Huyen | 2025 | Aplicaciones con foundation models: evaluación, RAG, fine-tuning |
| Understanding Deep Learning | S. J. D. Prince | 2023 | Gratis en línea; capítulos de transformers y difusión |

### Prácticos

| Título | Autores | Año | Aporte al LLM |
|---|---|---|---|
| Documentación de Hugging Face (Transformers, PEFT, TRL, Datasets) | Hugging Face | 2025 | Referencia práctica de fine-tuning y datos |
| nanoGPT / minGPT | A. Karpathy | 2023 | Implementaciones mínimas y legibles |
| The Illustrated Transformer (blog) | J. Alammar | 2018 | Intuición visual de la arquitectura |

## Papers clave

- Vaswani et al. (2017) — Attention Is All You Need
- Radford et al. (2019) — GPT-2
- Brown et al. (2020) — GPT-3 / few-shot
- Kaplan et al. (2020) — Scaling Laws for Neural Language Models
- Hoffmann et al. (2022) — Chinchilla
- Ouyang et al. (2022) — InstructGPT / RLHF
- Rafailov et al. (2023) — DPO
- Hu et al. (2021) — LoRA
- Dettmers et al. (2023) — QLoRA
- Lewis et al. (2020) — RAG
- Wei et al. (2022) — Chain-of-Thought Prompting
- Touvron et al. (2023) — Llama 2

## Datos, librerías y fuentes de texto

Fuentes que sí usa el corpus ([configs/data.yaml](../../configs/data.yaml)): Wikipedia es/en, FineWeb-2 `spa_Latn` y FineWeb-Edu `sample-10BT` (ODC-BY), Cosmopedia v2 (de SmolLM-corpus), OpenWebMath, abstracts de arXiv (`cs.CL`, `cs.LG`, `cs.AI`…) y codeparrot-clean, más el corpus personal y el semilla. Benchmarks de evaluación (no se entrenan): MMLU, HellaSwag, ARC, GSM8K, HumanEval.

## Vocabulario que debe dominar el modelo

*token*, *perplejidad*, *atención causal*, *KV cache*, *SFT*, *RLHF*, *DPO*, *LoRA*, *RAG*, *ventana de contexto*, *alucinación*, *leyes de escalado*

> Licencias: los libros guían temas y vocabulario y su texto no se ingiere; el texto del corpus sale solo de las fuentes de [configs/data.yaml](../../configs/data.yaml) (ver índice maestro).
