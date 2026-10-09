"""Supervised Fine-Tuning (SFT) del modelo pre-entrenado → asistente estilo chat.

Toma ``datasets/sft/{train,val}.jsonl`` (formato messages, ver build_sft.py),
aplica la plantilla ChatML de ``llm_lab.finetuning.chat`` y entrena SOLO sobre
los tokens de la respuesta (el prompt va enmascarado con -100).

    python scripts/sft.py --run checkpoints/small --epochs 4
    python scripts/sample.py --run checkpoints/small-sft --chat "¿Qué diferencia hay entre RAG y fine-tuning?"

Con 39 ejemplos semilla esto enseña el FORMATO de respuesta, no conocimiento
nuevo: el conocimiento viene del pre-entrenamiento. Para un asistente útil,
amplía datasets/sft (ver docs/07 → "Siguiente nivel").
"""

from __future__ import annotations

import argparse
import json
import math
import random
import shutil
import sys
from pathlib import Path

import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from llm_lab.finetuning.chat import build_sft_example  # noqa: E402
from llm_lab.training.trainer import configure_optimizer  # noqa: E402
from llm_lab.utils.hardware import get_device  # noqa: E402
from llm_lab.utils.seed import set_seed  # noqa: E402

sys.path.insert(0, str(ROOT / "scripts"))
from sample import load_run  # noqa: E402


def load_examples(path: Path, tok, max_len: int) -> list[dict]:
    encode = lambda s: tok.encode(s).ids  # noqa: E731
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return [build_sft_example(r["messages"], encode, max_len=max_len + 1) for r in rows]


def collate(batch: list[dict], pad_id: int):
    """Desplaza una posición: x = ids[:-1], y = labels[1:] (next-token)."""
    T = max(len(b["input_ids"]) for b in batch) - 1
    x = torch.full((len(batch), T), pad_id, dtype=torch.long)
    y = torch.full((len(batch), T), -100, dtype=torch.long)
    for i, b in enumerate(batch):
        ids, lab = b["input_ids"], b["labels"]
        x[i, :len(ids) - 1] = torch.tensor(ids[:-1])
        y[i, :len(lab) - 1] = torch.tensor(lab[1:])
    return x, y


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, help="carpeta del pre-entrenamiento")
    ap.add_argument("--out_dir", default=None)
    ap.add_argument("--data_dir", default=str(ROOT / "datasets" / "sft"))
    ap.add_argument("--epochs", type=int, default=4)
    ap.add_argument("--batch_size", type=int, default=8)
    ap.add_argument("--lr", type=float, default=1e-4)
    args = ap.parse_args()

    set_seed(42, deterministic_cudnn=False)
    device = get_device()
    run = Path(args.run)
    out_dir = Path(args.out_dir) if args.out_dir else run.with_name(run.name + "-sft")
    out_dir.mkdir(parents=True, exist_ok=True)

    model, tok = load_run(run, "best.pt", device)
    max_len = model.config.max_seq_len
    pad_id = tok.token_to_id("<|pad|>")
    train = load_examples(Path(args.data_dir) / "train.jsonl", tok, max_len)
    val = load_examples(Path(args.data_dir) / "val.jsonl", tok, max_len)
    print(f"🎛️  SFT: {len(train)} train · {len(val)} val · {args.epochs} épocas · lr {args.lr}")

    opt = configure_optimizer(model, args.lr, weight_decay=0.0, betas=(0.9, 0.95))
    total = args.epochs * math.ceil(len(train) / args.batch_size)
    sched = torch.optim.lr_scheduler.LambdaLR(opt, lambda s: 0.5 * (1 + math.cos(math.pi * s / total)))

    def val_loss() -> float:
        model.eval()
        with torch.no_grad():
            losses = [model(*[t.to(device) for t in collate(val[i:i + args.batch_size], pad_id)])[1].item()
                      for i in range(0, len(val), args.batch_size)]
        model.train()
        return sum(losses) / max(len(losses), 1)

    print(f"   val loss inicial {val_loss():.4f}")
    model.train()
    for epoch in range(args.epochs):
        random.shuffle(train)
        for i in range(0, len(train), args.batch_size):
            x, y = collate(train[i:i + args.batch_size], pad_id)
            _, loss = model(x.to(device), y.to(device))
            opt.zero_grad(set_to_none=True)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            opt.step()
            sched.step()
        print(f"   época {epoch + 1}: train {loss.item():.4f} · val {val_loss():.4f}")

    torch.save({"model_state_dict": model.state_dict(), "step": total}, out_dir / "best.pt")
    for f in ("tokenizer.json", "model_config.json"):
        shutil.copy(run / f, out_dir / f)
    print(f"→ {out_dir}")


if __name__ == "__main__":
    main()
