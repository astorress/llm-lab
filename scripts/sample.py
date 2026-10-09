"""Genera texto con un checkpoint entrenado.

    python scripts/sample.py --run checkpoints/small --prompt "La metaheurística NSGA-II"
    python scripts/sample.py --run checkpoints/small-sft --chat "¿Qué es el análisis de cohortes?"
    python scripts/sample.py --run checkpoints/small --interactive

``--run`` es la carpeta del entrenamiento (contiene best.pt/last.pt,
tokenizer.json y model_config.json).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from llm_lab.finetuning.chat import format_chat  # noqa: E402
from llm_lab.model.gpt import GPTConfig, MiniGPT  # noqa: E402
from llm_lab.tokenization.hf_tokenizer import load_tokenizer  # noqa: E402
from llm_lab.utils.hardware import get_device  # noqa: E402


def load_run(run: Path, which: str, device):
    cfg = GPTConfig(**json.loads((run / "model_config.json").read_text()))
    model = MiniGPT(cfg)
    ckpt_path = run / which if (run / which).exists() else run / "last.pt"
    state = torch.load(ckpt_path, map_location="cpu", weights_only=False)["model_state_dict"]
    model.load_state_dict(state)
    return model.to(device).eval(), load_tokenizer(run / "tokenizer.json")


def generate(model, tok, text: str, args, device, stop: str | None = None) -> str:
    ids = torch.tensor([tok.encode(text).ids], device=device)
    eos = tok.token_to_id(stop) if stop else tok.token_to_id("<|endoftext|>")
    out = model.generate(ids, max_new_tokens=args.max_new_tokens, temperature=args.temperature,
                         top_k=args.top_k, top_p=args.top_p, eos_token=eos)
    completion = tok.decode(out[0, ids.shape[1]:].tolist())
    return completion.split(stop)[0] if stop else completion


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--ckpt", default="best.pt")
    ap.add_argument("--prompt")
    ap.add_argument("--chat", help="pregunta en formato chat (modelo tras SFT)")
    ap.add_argument("--interactive", action="store_true")
    ap.add_argument("--max_new_tokens", type=int, default=200)
    ap.add_argument("--temperature", type=float, default=0.8)
    ap.add_argument("--top_k", type=int, default=50)
    ap.add_argument("--top_p", type=float, default=0.95)
    args = ap.parse_args()

    device = get_device()
    model, tok = load_run(Path(args.run), args.ckpt, device)

    def answer(q: str) -> str:
        if args.chat is not None or args.interactive:
            prompt = format_chat([{"role": "user", "content": q}], add_generation_prompt=True)
            return generate(model, tok, prompt, args, device, stop="<|im_end|>")
        return q + generate(model, tok, q, args, device)

    if args.interactive:
        print("Escribe una pregunta (Ctrl-D para salir).")
        for line in sys.stdin:
            print("→", answer(line.strip()), "\n")
    else:
        print(answer(args.chat or args.prompt or "La estadística bayesiana"))


if __name__ == "__main__":
    main()
