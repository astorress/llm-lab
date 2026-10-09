"""Fine-tuning (Fase 7): LoRA desde cero y plantillas de chat / SFT."""

from llm_lab.finetuning.chat import build_sft_example, format_chat
from llm_lab.finetuning.lora import (
    LoRALinear,
    count_trainable,
    inject_lora,
    mark_only_lora_trainable,
    merge_lora,
)

__all__ = [
    "LoRALinear",
    "inject_lora",
    "merge_lora",
    "mark_only_lora_trainable",
    "count_trainable",
    "format_chat",
    "build_sft_example",
]
