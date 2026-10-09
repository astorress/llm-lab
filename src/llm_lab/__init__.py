"""llm_lab — Laboratorio de construcción y entrenamiento de LLMs desde cero (Etapa 1).

Paquete espejo del código desarrollado en los notebooks 00–08.
Cada submódulo corresponde a una fase del proyecto:

- utils:         seeds, logging, detección de hardware, carga de configs
- data:          construcción de corpus (Fase 3)
- tokenization:  tokenizadores BPE/WordPiece/Unigram (Fase 2)
- embeddings:    Word2Vec desde cero, proyecciones, similitud (Fase 4)
- model:         transformer decoder-only desde cero (Fase 5)
- training:      loops de entrenamiento, schedulers, checkpointing (Fase 6)
- finetuning:    SFT, LoRA, chat templates (Fase 7)
- evaluation:    perplexity, BLEU/ROUGE, benchmarks (Fase 8)
- visualization: attention maps, gradient flow, curvas de entrenamiento
"""

__version__ = "0.1.0"
