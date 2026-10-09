"""Pre-entrena el MiniGPT del laboratorio sobre el corpus tokenizado del perfil.

    python scripts/pretrain.py --profile tiny                       # smoke test CPU
    python scripts/pretrain.py --profile small                      # T4 (Colab/Kaggle)
    python scripts/pretrain.py --profile large                      # A100 / 4090
    python scripts/pretrain.py --profile small --out_dir /content/drive/MyDrive/llm-lab/runs/small

Reanuda automáticamente si ``<out_dir>/last.pt`` existe (usa --fresh para
empezar de cero). Guarda ``last.pt`` cada ``checkpoint_every_steps`` y
``best.pt`` cuando mejora la val loss. Logs en ``<out_dir>/logs/*.jsonl``.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from dataclasses import asdict
from pathlib import Path

import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from llm_lab.data.loader import TokenDataset  # noqa: E402
from llm_lab.model.gpt import MiniGPT  # noqa: E402
from llm_lab.pipeline import ProfilePaths, build_model_config, load_profile  # noqa: E402
from llm_lab.tokenization.hf_tokenizer import load_tokenizer  # noqa: E402
from llm_lab.training.trainer import Trainer, TrainConfig  # noqa: E402
from llm_lab.utils.hardware import detect_hardware, get_device  # noqa: E402
from llm_lab.utils.seed import set_seed  # noqa: E402

SAMPLE_PROMPTS = [
    "La inferencia bayesiana actualiza una distribución a priori",
    "Un algoritmo genético para optimizar",
    "def train_model(",
]


def parse_repeat(spec: str) -> dict[str, float]:
    """'personal=1,seed=4' → {'personal': 1.0, 'seed': 4.0}."""
    pairs = [kv.split("=") for kv in spec.split(",") if kv.strip()]
    return {k.strip(): float(v) for k, v in pairs}


def resolve_precision(requested: str, device: torch.device) -> str:
    if device.type != "cuda":
        return "fp32"
    if requested == "bf16" and not torch.cuda.is_bf16_supported():
        print("⚠️  GPU sin bf16 → usando fp16")
        return "fp16"
    return requested


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--profile", default="tiny")
    ap.add_argument("--out_dir", default=None)
    ap.add_argument("--fresh", action="store_true", help="ignora last.pt y empieza de cero")
    ap.add_argument("--max_steps", type=int)
    ap.add_argument("--batch_size", type=int)
    ap.add_argument("--grad_accum", type=int)
    ap.add_argument("--lr", type=float, help="learning rate pico (pisa el del perfil)")
    ap.add_argument("--repeat", default="",
                    help="re-pondera fuentes sin re-tokenizar, p.ej. 'personal=1,seed=4'")
    ap.add_argument("--compile", action=argparse.BooleanOptionalAction, default=None)
    args = ap.parse_args()

    cfg = load_profile(args.profile)
    tcfg = cfg["training"]
    for key, val in [("max_steps", args.max_steps), ("batch_size", args.batch_size),
                     ("gradient_accumulation_steps", args.grad_accum), ("compile", args.compile),
                     ("lr", args.lr)]:
        if val is not None:
            tcfg[key] = val

    paths = ProfilePaths.for_profile(args.profile)
    out_dir = Path(args.out_dir) if args.out_dir else paths.checkpoints
    out_dir.mkdir(parents=True, exist_ok=True)

    set_seed(cfg["project"]["seed"], deterministic_cudnn=False)  # cudnn determinista = lento
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True
    detect_hardware()
    device = get_device()
    precision = resolve_precision(tcfg["mixed_precision"], device)

    data = TokenDataset(paths.tokenized, block_size=cfg["model"]["max_seq_len"],
                        seed=cfg["project"]["seed"], repeat=parse_repeat(args.repeat))
    tokenizer = load_tokenizer(paths.tokenizer)
    mcfg = build_model_config(cfg, vocab_size=data.meta["vocab_size"])
    model = MiniGPT(mcfg)

    n_params = model.count_parameters()
    tokens_per_step = tcfg["batch_size"] * mcfg.max_seq_len * tcfg["gradient_accumulation_steps"]
    planned = tokens_per_step * tcfg["max_steps"]
    print(f"\n🧠 MiniGPT {n_params['total'] / 1e6:.1f} M parámetros "
          f"({n_params['total_no_embeddings'] / 1e6:.1f} M sin embeddings)")
    print(f"📊 {data.meta['effective_train_tokens'] / 1e6:.0f} M tokens disponibles · "
          f"{planned / 1e6:.0f} M planificados · {planned / n_params['total']:.1f} tokens/parámetro")
    print(f"🎛️  mezcla: {data.mixture()}")
    print(f"⚙️  device {device} · {precision} · tokens/paso {tokens_per_step:,} · out {out_dir}\n")

    # Artefactos para que la carpeta del run sea autocontenida (sample/sft/export).
    shutil.copy(paths.tokenizer, out_dir / "tokenizer.json")
    (out_dir / "model_config.json").write_text(json.dumps(asdict(mcfg), indent=2))

    B = tcfg["batch_size"]
    eval_iters = tcfg.get("eval_iters", 50)
    amp_dtype = torch.bfloat16 if precision == "bf16" else torch.float16

    def get_batch():
        x, y = data.get_batch(B)
        if device.type == "cuda":
            return x.pin_memory(), y.pin_memory()
        return x, y

    def eval_fn(m) -> dict:
        out = {}
        for split in data.val:
            losses = []
            for _ in range(eval_iters):
                x, y = data.get_batch(B, split=split)
                with torch.autocast(device.type, dtype=amp_dtype, enabled=precision != "fp32"):
                    _, loss = m(x.to(device), y.to(device))
                losses.append(loss.item())
            mean = sum(losses) / len(losses)
            key = "val_loss" if split == "val" else f"{split}_loss"
            out[key] = mean
            out[key.replace("loss", "ppl")] = float(torch.exp(torch.tensor(mean)))
        return out

    def sample_fn(m) -> str:
        texts = []
        for prompt in SAMPLE_PROMPTS:
            ids = torch.tensor([tokenizer.encode(prompt).ids], device=device)
            outs = m.generate(ids, max_new_tokens=48, temperature=0.8, top_k=50)
            texts.append("   » " + tokenizer.decode(outs[0].tolist()).replace("\n", " "))
        return "\n".join(texts)

    train_cfg = TrainConfig(
        max_steps=tcfg["max_steps"], lr=tcfg["lr"], min_lr_ratio=tcfg.get("min_lr_ratio", 0.1),
        weight_decay=tcfg["weight_decay"], warmup_steps=tcfg["warmup_steps"],
        grad_clip_norm=tcfg["grad_clip_norm"], grad_accum_steps=tcfg["gradient_accumulation_steps"],
        eval_every=tcfg["eval_every_steps"], log_every=cfg["logging"]["log_every_steps"],
        checkpoint_every=tcfg.get("checkpoint_every_steps", 0), mixed_precision=precision,
        run_name=args.profile, out_dir=str(out_dir), tokens_per_step=tokens_per_step,
    )
    trainer = Trainer(model, train_cfg, device, get_batch, eval_fn=eval_fn, sample_fn=sample_fn,
                      data_state=data, model_config=asdict(mcfg),
                      compile_model=bool(tcfg.get("compile")) and device.type == "cuda")

    last = out_dir / "last.pt"
    if last.exists() and not args.fresh:
        trainer.load(last)
    trainer.train()
    print(f"\n✅ Listo. Mejor val loss {trainer.best_val:.4f} → {out_dir / 'best.pt'}")


if __name__ == "__main__":
    main()
