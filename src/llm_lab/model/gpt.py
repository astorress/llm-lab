"""MiniGPT: transformer decoder-only desde cero (Fase 5).

La arquitectura de GPT-2/Llama/Qwen a escala de laboratorio. Configurable vía
``GPTConfig``, alineada con ``configs/small.yaml`` y ``configs/large.yaml``.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import torch
import torch.nn.functional as F
from torch import nn

from llm_lab.model.layers import RMSNorm, TransformerBlock

__all__ = ["GPTConfig", "MiniGPT"]


@dataclass
class GPTConfig:
    """Hiperparámetros del modelo. Defaults = perfil SMALL (~4M params)."""

    vocab_size: int = 8000
    d_model: int = 256
    n_layers: int = 4
    n_heads: int = 4
    n_kv_heads: int | None = None   # None = MHA; <n_heads = GQA
    d_ff: int = 1024
    max_seq_len: int = 256
    dropout: float = 0.1
    tie_embeddings: bool = True     # comparte W_emb con la capa de salida
    positional: str = "rope"        # "rope" | "sinusoidal" | "learned"
    use_sdpa: bool = False          # kernel fusionado de PyTorch (Flash)
    swiglu: bool = False


class MiniGPT(nn.Module):
    """Modelo de lenguaje decoder-only.

    Flujo: tokens -> embedding (+ posicional si no es RoPE) -> N bloques
    -> norm final -> proyección al vocabulario (lm_head).
    """

    def __init__(self, config: GPTConfig):
        super().__init__()
        self.config = config
        self.tok_emb = nn.Embedding(config.vocab_size, config.d_model)

        # RoPE inyecta posición dentro de la atención; las otras opciones suman
        # un embedding posicional a la entrada.
        if config.positional == "learned":
            self.pos_emb = nn.Embedding(config.max_seq_len, config.d_model)
        else:
            self.pos_emb = None
        self.use_rope = config.positional == "rope"

        self.drop = nn.Dropout(config.dropout)
        self.blocks = nn.ModuleList([
            TransformerBlock(
                d_model=config.d_model,
                n_heads=config.n_heads,
                d_ff=config.d_ff,
                n_kv_heads=config.n_kv_heads,
                dropout=config.dropout,
                use_rope=self.use_rope,
                use_sdpa=config.use_sdpa,
                swiglu=config.swiglu,
                max_seq_len=config.max_seq_len,
            )
            for _ in range(config.n_layers)
        ])
        self.norm_f = RMSNorm(config.d_model)
        self.lm_head = nn.Linear(config.d_model, config.vocab_size, bias=False)

        if config.tie_embeddings:
            # Weight tying: la matriz de embedding ES la de salida (Press & Wolf,
            # 2017). Ahorra vocab_size·d_model parámetros y suele mejorar PPL.
            self.lm_head.weight = self.tok_emb.weight

        if config.positional == "sinusoidal":
            from llm_lab.model.positional import sinusoidal_encoding
            self.register_buffer(
                "_sinusoidal",
                sinusoidal_encoding(config.max_seq_len, config.d_model),
                persistent=False,
            )

        self.apply(self._init_weights)
        # Inicialización escalada de las proyecciones residuales (GPT-2): los
        # pesos que escriben al flujo residual se reducen por 1/√(2·n_layers)
        # para que la varianza de las activaciones no crezca con la profundidad.
        for name, p in self.named_parameters():
            if name.endswith("w_o.weight") or name.endswith("w_down.weight"):
                nn.init.normal_(p, mean=0.0, std=0.02 / math.sqrt(2 * config.n_layers))

    def _init_weights(self, module: nn.Module) -> None:
        if isinstance(module, nn.Linear):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def forward(
        self,
        idx: torch.Tensor,
        targets: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor | None]:
        """idx: (B, T) ids de token. Devuelve (logits (B,T,vocab), loss|None).

        Si se pasan ``targets`` (B, T), calcula la cross-entropy de
        next-token prediction (ignora -100, usado para enmascarar el prompt
        en SFT).
        """
        B, T = idx.shape
        x = self.tok_emb(idx)  # (B,T,C)
        if self.pos_emb is not None:
            pos = torch.arange(T, device=idx.device)
            x = x + self.pos_emb(pos)[None, :, :]
        elif self.config.positional == "sinusoidal":
            x = x + self._sinusoidal[:T][None, :, :].to(x.dtype)
        x = self.drop(x)

        for block in self.blocks:
            x = block(x)
        x = self.norm_f(x)
        logits = self.lm_head(x)  # (B,T,vocab)

        loss = None
        if targets is not None:
            loss = F.cross_entropy(
                logits.view(-1, logits.size(-1)),
                targets.view(-1),
                ignore_index=-100,
            )
        return logits, loss

    def count_parameters(self) -> dict[str, int]:
        """Desglosa el nº de parámetros por componente (para tablas/gráficos)."""
        def n(p_iter):
            return sum(p.numel() for p in p_iter)

        emb = self.tok_emb.weight.numel()
        pos = self.pos_emb.weight.numel() if self.pos_emb is not None else 0
        blocks = n(self.blocks.parameters())
        norm = n(self.norm_f.parameters())
        # Con tie_embeddings, lm_head comparte memoria con tok_emb (no se suma).
        head = 0 if self.config.tie_embeddings else self.lm_head.weight.numel()
        total = sum(p.numel() for p in self.parameters())
        return {
            "token_embeddings": emb,
            "positional_embeddings": pos,
            "transformer_blocks": blocks,
            "final_norm": norm,
            "lm_head": head,
            "total": total,
            "total_no_embeddings": blocks + norm,
        }

    @torch.no_grad()
    def generate(
        self,
        idx: torch.Tensor,
        max_new_tokens: int,
        temperature: float = 1.0,
        top_k: int | None = None,
        top_p: float | None = None,
        eos_token: int | None = None,
    ) -> torch.Tensor:
        """Generación autoregresiva. idx: (B, T0) prompt. Devuelve (B, T0+n).

        - temperature: divide los logits; <1 más conservador, >1 más diverso.
        - top_k: muestrea solo de los k tokens más probables.
        - top_p (nucleus): muestrea del menor conjunto cuya prob acumulada ≥ p.
        """
        self.eval()
        for _ in range(max_new_tokens):
            # Recorta el contexto a la ventana máxima del modelo.
            idx_cond = idx[:, -self.config.max_seq_len:]
            logits, _ = self(idx_cond)
            logits = logits[:, -1, :]  # (B, vocab) — solo la última posición

            if temperature != 1.0:
                logits = logits / max(temperature, 1e-6)

            if top_k is not None:
                kth = torch.topk(logits, min(top_k, logits.size(-1)))[0][:, -1, None]
                logits = logits.masked_fill(logits < kth, float("-inf"))

            if top_p is not None:
                sorted_logits, sorted_idx = torch.sort(logits, descending=True, dim=-1)
                cum = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)
                remove = cum > top_p
                # Conservar siempre al menos el token más probable.
                remove[:, 1:] = remove[:, :-1].clone()
                remove[:, 0] = False
                sorted_logits = sorted_logits.masked_fill(remove, float("-inf"))
                logits = torch.full_like(logits, float("-inf")).scatter(
                    1, sorted_idx, sorted_logits
                )

            probs = F.softmax(logits, dim=-1)
            if temperature == 0:
                next_tok = torch.argmax(probs, dim=-1, keepdim=True)
            else:
                next_tok = torch.multinomial(probs, num_samples=1)
            idx = torch.cat([idx, next_tok], dim=1)

            if eos_token is not None and (next_tok == eos_token).all():
                break
        return idx
