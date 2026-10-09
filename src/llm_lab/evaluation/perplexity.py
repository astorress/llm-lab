"""Perplexity (Fase 8).

PPL = exp(CE), la cross-entropy media por token exponenciada. Se interpreta
como el "branching factor" efectivo: cuántos tokens equiprobables, en promedio,
el modelo considera en cada paso. Menor = mejor.

Para secuencias más largas que la ventana del modelo se usa una ventana
deslizante con solapamiento (stride): cada token se predice con el máximo
contexto posible, evitando el sesgo de evaluar tokens iniciales sin contexto.
"""

from __future__ import annotations

import math

import torch

__all__ = ["compute_perplexity", "sliding_window_perplexity"]


@torch.no_grad()
def compute_perplexity(model, input_ids: torch.Tensor, device=None) -> float:
    """PPL sobre una única secuencia (1D o (1, T)) que cabe en el contexto."""
    model.eval()
    if input_ids.dim() == 1:
        input_ids = input_ids.unsqueeze(0)
    if device is not None:
        input_ids = input_ids.to(device)
    inputs = input_ids[:, :-1]
    targets = input_ids[:, 1:]
    _, loss = model(inputs, targets)
    return math.exp(loss.item())


@torch.no_grad()
def sliding_window_perplexity(
    model,
    token_ids: list[int] | torch.Tensor,
    max_len: int,
    stride: int | None = None,
    device=None,
) -> float:
    """PPL sobre una secuencia larga con ventana deslizante.

    stride controla el solapamiento: stride=max_len no solapa (peor estimación);
    stride pequeño solapa mucho (mejor estimación, más cómputo). Los tokens ya
    contabilizados en una ventana previa se enmascaran con -100.
    """
    model.eval()
    if isinstance(token_ids, list):
        token_ids = torch.tensor(token_ids, dtype=torch.long)
    if device is not None:
        token_ids = token_ids.to(device)
    stride = stride or max_len // 2
    n = token_ids.size(0)

    nll_sum, n_tokens, prev_end = 0.0, 0, 0
    for begin in range(0, n, stride):
        end = min(begin + max_len, n)
        trg_len = end - prev_end  # tokens nuevos en esta ventana
        window = token_ids[begin:end].unsqueeze(0)
        if window.size(1) < 2:
            break
        target = window.clone()
        # Enmascarar los tokens ya evaluados en ventanas previas.
        target[:, :-trg_len] = -100
        _, loss = model(window[:, :-1], target[:, 1:])
        # loss es media sobre tokens no enmascarados de esta ventana.
        valid = (target[:, 1:] != -100).sum().item()
        nll_sum += loss.item() * valid
        n_tokens += valid
        prev_end = end
        if end == n:
            break
    return math.exp(nll_sum / max(n_tokens, 1))
