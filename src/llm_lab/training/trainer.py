"""Trainer: loop de pre-entrenamiento industrial (Fase 6).

Reúne las piezas que un entrenamiento real necesita y que se estudian una a una
en el notebook 06: precisión mixta (autocast + GradScaler), acumulación de
gradiente, recorte de gradiente, weight decay selectivo (el "truco" de GPT-2 de
no decaer biases ni normas), scheduler warmup+cosine, logging a JSONL,
evaluación periódica y checkpoints reanudables.

Reanudación: ``Trainer.load(path)`` restaura pesos, optimizador, scheduler,
GradScaler, RNGs y (opcional) el estado del DataLoader, de modo que una sesión
de Colab cortada continúa exactamente donde quedó.
"""

from __future__ import annotations

import math
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable

import torch
from torch import nn

from llm_lab.training.checkpoint import load_checkpoint, save_checkpoint
from llm_lab.training.scheduler import WarmupCosineScheduler
from llm_lab.utils.logging import MetricsLogger, get_logger

__all__ = ["TrainConfig", "Trainer", "configure_optimizer"]


@dataclass
class TrainConfig:
    max_steps: int = 3000
    lr: float = 3e-4
    min_lr_ratio: float = 0.1          # lr_min = lr · min_lr_ratio al final del coseno
    weight_decay: float = 0.1
    warmup_steps: int = 200
    grad_clip_norm: float = 1.0
    grad_accum_steps: int = 1
    eval_every: int = 200
    log_every: int = 10
    checkpoint_every: int = 0          # 0 = solo al final
    mixed_precision: str = "fp32"      # "fp32" | "fp16" | "bf16"
    betas: tuple[float, float] = (0.9, 0.95)
    run_name: str = "run"
    out_dir: str = "checkpoints/run"
    tokens_per_step: int = 0           # B·T·accum, solo para reportar tokens/s


def configure_optimizer(model: nn.Module, lr: float, weight_decay: float, betas) -> torch.optim.Optimizer:
    """AdamW con weight decay SOLO en matrices 2D (no en biases ni en normas).

    El truco de GPT-2/nanoGPT: decaer biases y ganancias de LayerNorm/RMSNorm
    perjudica; estos parámetros (1D) van en un grupo con weight_decay=0.
    """
    decay, no_decay = [], []
    for _, p in model.named_parameters():
        if not p.requires_grad:
            continue
        (decay if p.dim() >= 2 else no_decay).append(p)
    groups = [
        {"params": decay, "weight_decay": weight_decay},
        {"params": no_decay, "weight_decay": 0.0},
    ]
    # fused=True: un solo kernel CUDA para todo el update (≈10 % más rápido).
    fused = torch.cuda.is_available() and next(model.parameters()).is_cuda
    return torch.optim.AdamW(groups, lr=lr, betas=betas, fused=fused)


class Trainer:
    """Loop de entrenamiento reanudable.

    Args:
        model: el MiniGPT (o cualquier modelo cuyo forward devuelva (logits, loss)).
        cfg: TrainConfig.
        device: torch.device.
        get_batch: callable() -> (inputs, targets) ambos (B, T) en CPU o device.
        eval_fn: callable(model) -> dict de métricas (p.ej. {"val_loss": ...}).
        sample_fn: callable(model) -> str, texto generado para inspección cualitativa.
        data_state: objeto con state_dict()/load_state_dict() (el DataLoader) que
            se guarda en el checkpoint para reanudar el muestreo exacto.
        model_config: dict serializable con la arquitectura (va al checkpoint).
    """

    def __init__(self, model, cfg: TrainConfig, device, get_batch: Callable,
                 eval_fn: Callable | None = None, sample_fn: Callable | None = None,
                 data_state=None, model_config: dict | None = None, compile_model: bool = False):
        self.model = model.to(device)
        self.cfg = cfg
        self.device = device
        self.get_batch = get_batch
        self.eval_fn = eval_fn
        self.sample_fn = sample_fn
        self.data_state = data_state
        self.model_config = model_config or {}
        self.out_dir = Path(cfg.out_dir)
        self.logger = get_logger("trainer")
        self.metrics = MetricsLogger(cfg.run_name, log_dir=self.out_dir / "logs")

        self.optimizer = configure_optimizer(self.model, cfg.lr, cfg.weight_decay, cfg.betas)
        self.scheduler = WarmupCosineScheduler(
            self.optimizer, cfg.lr, cfg.warmup_steps, cfg.max_steps, lr_min=cfg.lr * cfg.min_lr_ratio
        )
        # GradScaler solo tiene sentido en fp16 (bf16 tiene el rango de fp32).
        self.use_amp = cfg.mixed_precision in ("fp16", "bf16") and device.type == "cuda"
        self.amp_dtype = torch.bfloat16 if cfg.mixed_precision == "bf16" else torch.float16
        self.scaler = torch.amp.GradScaler(
            "cuda", enabled=self.use_amp and cfg.mixed_precision == "fp16"
        )
        # El modelo compilado comparte parámetros con self.model: se guarda self.model.
        self.fwd_model = torch.compile(self.model) if compile_model else self.model
        self.step = 0
        self.best_val = math.inf

    # ── checkpoints ───────────────────────────────────────────────
    def save(self, name: str = "last.pt", metrics: dict | None = None) -> Path:
        path = save_checkpoint(
            self.out_dir / name, self.step, self.model, self.optimizer, self.scheduler, self.scaler,
            config={"model": self.model_config, "train": asdict(self.cfg)},
            metrics={**(metrics or {}), "best_val": self.best_val},
        )
        if self.data_state is not None:
            ckpt = torch.load(path, map_location="cpu", weights_only=False)
            ckpt["data_state"] = self.data_state.state_dict()
            torch.save(ckpt, path)
        return path

    def load(self, path: str | Path) -> int:
        ckpt = load_checkpoint(path, self.model, self.optimizer, self.scheduler, self.scaler,
                               map_location=self.device)
        if self.data_state is not None and ckpt.get("data_state"):
            self.data_state.load_state_dict(ckpt["data_state"])
        self.step = ckpt["step"]
        self.best_val = ckpt.get("metrics", {}).get("best_val", math.inf)
        self.logger.info("Reanudando desde %s (step %d)", path, self.step)
        return self.step

    # ── loop ──────────────────────────────────────────────────────
    def _forward_loss(self, inputs, targets):
        if self.use_amp:
            with torch.autocast(device_type=self.device.type, dtype=self.amp_dtype):
                _, loss = self.fwd_model(inputs, targets)
        else:
            _, loss = self.fwd_model(inputs, targets)
        return loss

    def _evaluate(self) -> None:
        self.model.eval()
        with torch.no_grad():
            eval_metrics = self.eval_fn(self.fwd_model) if self.eval_fn else {}
        self.metrics.log(self.step, **eval_metrics)
        self.logger.info("eval step %d | %s", self.step,
                         " | ".join(f"{k} {v:.4f}" for k, v in eval_metrics.items()))
        val = eval_metrics.get("val_loss")
        if val is not None and val < self.best_val:
            self.best_val = val
            self.save("best.pt", eval_metrics)
        if self.sample_fn is not None:
            self.logger.info("muestra:\n%s", self.sample_fn(self.model))
        self.model.train()

    def train(self, max_steps: int | None = None) -> MetricsLogger:
        """Entrena hasta ``max_steps`` (o cfg.max_steps). Reanudable: usa self.step."""
        target = max_steps or self.cfg.max_steps
        self.scheduler.step_num = self.step
        self.model.train()
        t0 = time.time()
        while self.step < target:
            lr = self.scheduler.step()
            self.optimizer.zero_grad(set_to_none=True)

            accum_loss = 0.0
            for _ in range(self.cfg.grad_accum_steps):
                inputs, targets = self.get_batch()
                inputs = inputs.to(self.device, non_blocking=True)
                targets = targets.to(self.device, non_blocking=True)
                loss = self._forward_loss(inputs, targets) / self.cfg.grad_accum_steps
                self.scaler.scale(loss).backward()
                accum_loss += loss.item()

            # Recorte de gradiente: requiere des-escalar primero si hay scaler.
            if self.cfg.grad_clip_norm > 0:
                self.scaler.unscale_(self.optimizer)
                grad_norm = nn.utils.clip_grad_norm_(self.model.parameters(), self.cfg.grad_clip_norm)
            else:
                grad_norm = torch.tensor(0.0)

            self.scaler.step(self.optimizer)
            self.scaler.update()
            self.step += 1

            if self.step % self.cfg.log_every == 0 or self.step == 1:
                dt = time.time() - t0
                t0 = time.time()
                n = self.cfg.log_every if self.step > 1 else 1
                tok_s = self.cfg.tokens_per_step * n / max(dt, 1e-9)
                self.metrics.log(self.step, loss=accum_loss, lr=lr,
                                 grad_norm=float(grad_norm), tokens_per_sec=round(tok_s))
                self.logger.info("step %5d/%d | loss %.4f | lr %.2e | gnorm %.2f | %s tok/s",
                                 self.step, target, accum_loss, lr, float(grad_norm), f"{tok_s:,.0f}")

            if self.cfg.eval_every and self.step % self.cfg.eval_every == 0:
                self._evaluate()
            if self.cfg.checkpoint_every and self.step % self.cfg.checkpoint_every == 0:
                self.save("last.pt")

        self._evaluate()
        self.save("last.pt")
        return self.metrics
