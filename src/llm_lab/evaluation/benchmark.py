"""Benchmark multiple-choice por log-verosimilitud (Fase 8).

Estilo MMLU/lm-evaluation-harness: para cada pregunta se forma "pregunta +
opción" y se elige la opción con mayor log-probabilidad bajo el modelo (no se
genera texto libre). Es determinista y no depende del formato de salida.

Para usar con un modelo HuggingFace, pásale un ``score_fn(prompt, continuation)``
que devuelva el log-prob de la continuación; aquí se implementa el harness y la
agregación de métricas (accuracy global y por dominio).
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Callable

__all__ = ["MCQuestion", "MultipleChoiceBenchmark", "wilson_interval"]


@dataclass
class MCQuestion:
    question: str
    options: list[str]
    answer: int          # índice de la opción correcta
    domain: str = "general"


def wilson_interval(correct: int, total: int, z: float = 1.96) -> tuple[float, float]:
    """Intervalo de confianza de Wilson para una proporción (más robusto que el normal).

    Apropiado para accuracy con pocas muestras o proporciones cerca de 0/1.
    """
    if total == 0:
        return (0.0, 0.0)
    p = correct / total
    denom = 1 + z**2 / total
    center = (p + z**2 / (2 * total)) / denom
    margin = (z * ((p * (1 - p) / total + z**2 / (4 * total**2)) ** 0.5)) / denom
    return (max(0.0, center - margin), min(1.0, center + margin))


class MultipleChoiceBenchmark:
    """Evalúa un modelo sobre una lista de MCQuestion."""

    def __init__(self, questions: list[MCQuestion]):
        self.questions = questions

    def evaluate(self, score_fn: Callable[[str, str], float]) -> dict:
        """score_fn(prompt, continuation) -> logprob de la continuación.

        Devuelve accuracy global, por dominio, intervalos de Wilson y el detalle
        de predicciones.
        """
        per_domain = defaultdict(lambda: {"correct": 0, "total": 0})
        correct_total = 0
        preds = []
        for q in self.questions:
            prompt = q.question + "\nRespuesta:"
            scores = [score_fn(prompt, " " + opt) for opt in q.options]
            pred = max(range(len(q.options)), key=lambda i: scores[i])
            ok = pred == q.answer
            correct_total += int(ok)
            per_domain[q.domain]["total"] += 1
            per_domain[q.domain]["correct"] += int(ok)
            preds.append({"question": q.question, "pred": pred, "answer": q.answer, "correct": ok})

        n = len(self.questions)
        domain_acc = {
            d: {
                "accuracy": v["correct"] / max(v["total"], 1),
                "n": v["total"],
                "wilson": wilson_interval(v["correct"], v["total"]),
            }
            for d, v in per_domain.items()
        }
        return {
            "accuracy": correct_total / max(n, 1),
            "n": n,
            "wilson": wilson_interval(correct_total, n),
            "per_domain": domain_acc,
            "predictions": preds,
        }
