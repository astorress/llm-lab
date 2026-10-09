"""Chat templates y masking de prompt para SFT (Fase 7).

Un modelo solo ve tokens: los "roles" (system/user/assistant) son una
convención que se materializa con tokens especiales delimitadores. Aquí se usa
un formato estilo ChatML (<|im_start|>rol ... <|im_end|>).

En SFT se entrena la loss SOLO sobre los tokens de la respuesta del asistente:
los del prompt se enmascaran con -100 (ignore_index de cross_entropy). Así el
modelo aprende a RESPONDER, no a regenerar la pregunta.
"""

from __future__ import annotations

__all__ = ["format_chat", "build_sft_example", "IM_START", "IM_END"]

IM_START = "<|im_start|>"
IM_END = "<|im_end|>"


def format_chat(messages: list[dict], add_generation_prompt: bool = False) -> str:
    """Convierte [{"role","content"}] en un string ChatML.

    Si ``add_generation_prompt`` es True, deja el turno del asistente abierto
    (para inferencia): el modelo debe continuar generando la respuesta.
    """
    parts = []
    for m in messages:
        parts.append(f"{IM_START}{m['role']}\n{m['content']}{IM_END}\n")
    if add_generation_prompt:
        parts.append(f"{IM_START}assistant\n")
    return "".join(parts)


def build_sft_example(
    messages: list[dict],
    encode,
    max_len: int | None = None,
) -> dict:
    """Construye (input_ids, labels) para un ejemplo SFT con prompt enmascarado.

    Args:
        messages: la conversación; el ÚLTIMO mensaje debe ser del asistente
            (la respuesta a aprender).
        encode: callable(str) -> list[int].
        max_len: trunca si se indica.

    Returns:
        {"input_ids": [...], "labels": [...]} donde labels == -100 en los
        tokens del prompt y == input_ids en los de la respuesta.
    """
    if not messages or messages[-1]["role"] != "assistant":
        raise ValueError("El último mensaje debe ser del asistente (la respuesta).")

    # Prompt = todo menos la respuesta final, con el turno de asistente abierto.
    prompt_text = format_chat(messages[:-1], add_generation_prompt=True)
    full_text = format_chat(messages, add_generation_prompt=False)

    prompt_ids = encode(prompt_text)
    full_ids = encode(full_text)

    labels = [-100] * len(prompt_ids) + full_ids[len(prompt_ids):]
    if max_len is not None:
        full_ids = full_ids[:max_len]
        labels = labels[:max_len]
    return {"input_ids": full_ids, "labels": labels}
