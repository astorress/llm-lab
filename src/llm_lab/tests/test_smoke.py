"""Smoke tests del paquete llm_lab.

Verifican que las piezas centrales se importan, instancian y ejecutan sin error.
Los que necesitan PyTorch se saltan automáticamente si torch no está instalado
(``pytest.importorskip``), de modo que el resto del paquete sigue siendo testeable.

Ejecutar:  pytest src/llm_lab/tests/test_smoke.py
"""

from __future__ import annotations

import pytest


def test_data_pipeline_sin_torch():
    """Las utilidades de datos no requieren torch."""
    from llm_lab.data import exact_dedup, make_document, normalize_text, quality_score

    assert normalize_text("  hola   mundo ") == "hola mundo"
    d1 = make_document("El recocido simulado acepta soluciones peores al inicio.", "metaheuristica")
    d2 = make_document("El recocido simulado acepta soluciones peores al inicio.", "metaheuristica")
    assert d1["id"] == d2["id"]  # id determinista → mismo contenido, mismo id
    assert 0.0 <= quality_score(d1["content"]) <= 1.0
    assert len(exact_dedup([d1, d2])) == 1  # dedup exacta colapsa duplicados


def test_bpe_tokenizer():
    """BPE educacional: entrena y hace round-trip encode/decode."""
    from llm_lab.tokenization import BPETokenizer

    corpus = [
        "el transformador reduce el voltaje",
        "la red neuronal aprende por gradiente",
        "la armonia tonal del sistema musical",
        "descenso de gradiente estocastico",
        "voltaje y corriente en la subestacion",
    ]
    tok = BPETokenizer()
    tok.train(corpus, vocab_size=80)
    ids = tok.encode("el voltaje")
    assert isinstance(ids, list) and len(ids) > 0
    assert "voltaje" in tok.decode(tok.encode("voltaje"))


def test_text_metrics():
    """BLEU y ROUGE-L desde cero dan valores sensatos."""
    from llm_lab.evaluation import bleu_score, rouge_l

    ref = "el voltaje de la subestacion".split()
    assert bleu_score(ref, ref) == pytest.approx(1.0, abs=1e-6)
    r = rouge_l(ref, ref)
    assert r["f"] == pytest.approx(1.0, abs=1e-6)


def test_minigpt_forward_y_generate():
    """Núcleo del lab: MiniGPT instancia, hace forward con loss y genera."""
    torch = pytest.importorskip("torch")
    from llm_lab.model import GPTConfig, MiniGPT

    cfg = GPTConfig(vocab_size=100, d_model=32, n_layers=2, n_heads=4, d_ff=64, max_seq_len=32)
    model = MiniGPT(cfg)

    idx = torch.randint(0, 100, (2, 16))
    targets = torch.randint(0, 100, (2, 16))
    logits, loss = model(idx, targets)
    assert logits.shape == (2, 16, 100)
    assert torch.isfinite(loss)

    out = model.generate(idx[:, :4], max_new_tokens=10)
    assert out.shape == (2, 14)

    bd = model.count_parameters()
    assert bd["total"] > 0


def test_lora_inject_y_count():
    """LoRA desde cero: inyecta, congela base y cuenta entrenables."""
    torch = pytest.importorskip("torch")
    from llm_lab.finetuning import count_trainable, inject_lora, mark_only_lora_trainable
    from llm_lab.model import GPTConfig, MiniGPT

    model = MiniGPT(GPTConfig(vocab_size=100, d_model=32, n_layers=2, n_heads=4, d_ff=64, max_seq_len=32))
    n = inject_lora(model, ["w_q", "w_v"], r=4, alpha=8)
    assert n > 0
    mark_only_lora_trainable(model)
    stats = count_trainable(model)
    assert 0 < stats["trainable"] < stats["total"]


def test_scheduler_y_attention():
    """Scheduler warmup-cosine y attention causal desde cero."""
    torch = pytest.importorskip("torch")
    from llm_lab.model import scaled_dot_product_attention
    from llm_lab.training import warmup_cosine_lr

    # warmup sube, luego decae
    lr0 = warmup_cosine_lr(0, lr_max=1e-3, warmup_steps=10, total_steps=100)
    lr_peak = warmup_cosine_lr(10, lr_max=1e-3, warmup_steps=10, total_steps=100)
    lr_end = warmup_cosine_lr(100, lr_max=1e-3, warmup_steps=10, total_steps=100)
    assert lr0 < lr_peak and lr_end < lr_peak

    q = k = v = torch.randn(1, 2, 5, 8)
    out, w = scaled_dot_product_attention(q, k, v, causal=True)
    assert out.shape == (1, 2, 5, 8)
    # causal: la primera posición solo se atiende a sí misma
    assert torch.allclose(w[0, 0, 0, 1:], torch.zeros(4), atol=1e-6)


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
