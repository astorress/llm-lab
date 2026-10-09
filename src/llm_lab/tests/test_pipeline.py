"""Tests del pipeline de pre-entrenamiento: dominio, fuentes, loader y Trainer.

Ejecutar:  pytest src/llm_lab/tests/test_pipeline.py
"""

from __future__ import annotations

import json

import pytest


def test_domain_classifier_cuenta_terminos_distintos():
    from llm_lab.data.domains import DomainClassifier

    clf = DomainClassifier()
    tecnico = ("El algoritmo genético combina cruce y mutación según una función de aptitud; "
               "el recocido simulado y la búsqueda tabú son alternativas de búsqueda local.")
    m = clf.classify(tecnico)
    assert m.domain == "metaheuristica"
    assert m.total_hits >= 4
    # Repetir un término no suma: se cuentan términos DISTINTOS.
    assert clf.classify("voltaje " * 50).total_hits == 1
    assert clf.classify("Receta de arepas con queso y mantequilla.").total_hits == 0
    assert clf.classify("Kant fundó la ética del deber; Hume, el empirismo y la epistemología "
                        "escéptica.").domain == "filosofia"
    assert "sistemas_potencia" not in clf.domains


def test_iter_source_local_filtra_y_etiqueta(tmp_path):
    from llm_lab.data.domains import DomainClassifier
    from llm_lab.data.sources import iter_source

    rows = [
        {"text": "Texto corto"},
        {"text": "La red neuronal aprende con descenso de gradiente y backpropagation. " * 6},
    ]
    path = tmp_path / "src.jsonl"
    path.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
    spec = {"type": "local_jsonl", "path": "src.jsonl", "lang": "es", "min_domain_hits": 2}
    docs = list(iter_source("t", spec, tmp_path, DomainClassifier()))
    assert len(docs) == 1
    assert docs[0]["domain"] == "deep_learning" and docs[0]["source"] == "t"


def _write_bins(tmp_path, np):
    meta = {"vocab_size": 50, "dtype": "uint16", "eot_id": 0,
            "sources": {"a": {"train_tokens": 1000, "repeat": 1},
                        "b": {"train_tokens": 1000, "repeat": 3}}}
    for name, val in [("train_a", 1), ("train_b", 2)]:
        np.full(1000, val, dtype=np.uint16).tofile(tmp_path / f"{name}.bin")
    np.arange(500, dtype=np.uint16).tofile(tmp_path / "val.bin")
    (tmp_path / "meta.json").write_text(json.dumps(meta))


def test_token_dataset_mezcla_y_shapes(tmp_path):
    torch = pytest.importorskip("torch")
    import numpy as np

    from llm_lab.data.loader import TokenDataset

    _write_bins(tmp_path, np)
    ds = TokenDataset(tmp_path, block_size=16, seed=0)
    assert ds.mixture() == {"a": 0.25, "b": 0.75}   # p ∝ tokens · repeat
    x, y = ds.get_batch(400)
    assert x.shape == (400, 16) and x.dtype == torch.int64
    frac_b = (x[:, 0] == 2).float().mean().item()
    assert 0.65 < frac_b < 0.85
    # repeat pisa el de meta.json sin re-tokenizar
    assert TokenDataset(tmp_path, block_size=16, repeat={"b": 1}).mixture() == {"a": 0.5, "b": 0.5}
    xv, yv = ds.get_batch(4, split="val")
    assert torch.equal(xv[:, 1:], yv[:, :-1])          # y es x desplazado una posición


def test_trainer_aprende_y_reanuda(tmp_path):
    torch = pytest.importorskip("torch")
    import numpy as np

    from llm_lab.data.loader import TokenDataset
    from llm_lab.model import GPTConfig, MiniGPT
    from llm_lab.training import Trainer, TrainConfig

    # Secuencia periódica: un modelo pequeño debe aprenderla rápido.
    meta = {"vocab_size": 16, "dtype": "uint16", "eot_id": 0,
            "sources": {"p": {"train_tokens": 4000, "repeat": 1}}}
    np.tile(np.arange(16, dtype=np.uint16), 250).tofile(tmp_path / "train_p.bin")
    np.tile(np.arange(16, dtype=np.uint16), 20).tofile(tmp_path / "val.bin")
    (tmp_path / "meta.json").write_text(json.dumps(meta))

    def make():
        torch.manual_seed(0)
        ds = TokenDataset(tmp_path, block_size=16, seed=0)
        model = MiniGPT(GPTConfig(vocab_size=16, d_model=32, n_layers=1, n_heads=2,
                                  d_ff=64, max_seq_len=16, dropout=0.0, use_sdpa=True))
        cfg = TrainConfig(max_steps=60, lr=3e-3, warmup_steps=5, eval_every=0, log_every=20,
                          checkpoint_every=30, out_dir=str(tmp_path / "run"))

        def eval_fn(m):
            x, y = ds.get_batch(8, split="val")
            return {"val_loss": m(x, y)[1].item()}

        return Trainer(model, cfg, torch.device("cpu"), lambda: ds.get_batch(8),
                       eval_fn=eval_fn, data_state=ds)

    trainer = make()
    trainer.train(max_steps=30)
    resumed = make()
    assert resumed.load(tmp_path / "run" / "last.pt") == 30
    resumed.train()
    assert resumed.step == 60
    assert resumed.best_val < 1.0    # ln(16) ≈ 2.77 al azar
