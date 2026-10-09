# ──────────────────────────────────────────────────────────────────
# LLM Lab — atajos del pipeline. PROFILE = tiny | small | large
#   make data PROFILE=tiny && make train PROFILE=tiny     # smoke test (CPU, minutos)
#   make data PROFILE=small WORKERS=10                    # en el Mac / devcontainer
#   make train PROFILE=small OUT=/content/drive/MyDrive/llm-lab/runs/small   # en GPU
# ──────────────────────────────────────────────────────────────────
PROFILE ?= tiny
WORKERS ?= 4
PY      ?= python
OUT     ?=
RUN     ?= checkpoints/$(PROFILE)
OUT_ARG  = $(if $(OUT),--out_dir $(OUT),)

.PHONY: help personal seed corpus tokenizer tokenize data bundle train sft sample chat test smoke clean-profile jupyter

help:
	@grep -E '^[a-z-]+:.*##' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  %-14s %s\n", $$1, $$2}'

personal: ## Recolecta tu corpus personal (tesis, notebooks, código)
	$(PY) scripts/collect_personal_corpus.py

seed: ## Corpus semilla curado + dataset SFT
	$(PY) scripts/build_corpus.py && $(PY) scripts/build_sft.py

corpus: ## Descarga/filtra las fuentes del perfil → datasets/pretrain/<perfil>
	$(PY) scripts/build_pretrain_corpus.py --profile $(PROFILE) --workers $(WORKERS)

tokenizer: ## Entrena el BPE byte-level del perfil
	$(PY) scripts/train_tokenizer.py --profile $(PROFILE)

tokenize: ## Tokeniza a .bin (memmap)
	$(PY) scripts/tokenize_corpus.py --profile $(PROFILE)

data: personal seed corpus tokenizer tokenize ## Todo el pipeline de datos

bundle: ## Empaqueta código + Docker + tokenizer + .bin del perfil → dist/llm-lab-<perfil>.tar
	@mkdir -p dist
	tar -cf dist/llm-lab-$(PROFILE).tar --exclude='__pycache__' --exclude='*.pyc' \
	  src scripts configs Makefile pyproject.toml requirements.txt requirements-notebooks.txt \
	  .docker .dockerignore README.md datasets/sft \
	  datasets/schemas tokenizer/trained/$(PROFILE) datasets/tokenized/$(PROFILE)
	@ls -lh dist/llm-lab-$(PROFILE).tar

train: ## Pre-entrena (reanuda solo si existe last.pt)
	$(PY) scripts/pretrain.py --profile $(PROFILE) $(OUT_ARG)

sft: ## Fine-tuning instruccional sobre el mejor checkpoint
	$(PY) scripts/sft.py --run $(if $(OUT),$(OUT),$(RUN))

sample: ## Genera texto con el modelo pre-entrenado
	$(PY) scripts/sample.py --run $(if $(OUT),$(OUT),$(RUN)) --prompt "La optimización por enjambre de partículas"

chat: ## Chat interactivo con el modelo tras SFT
	$(PY) scripts/sample.py --run $(if $(OUT),$(OUT),$(RUN))-sft --interactive

test: ## Tests
	$(PY) -m pytest -q src/llm_lab/tests

smoke: ## Pipeline completo en tiny (CPU): datos + 300 pasos + SFT + muestra
	$(MAKE) data train sft sample PROFILE=tiny

clean-profile: ## Borra artefactos del perfil (pide confirmación)
	@read -p "¿Borrar datasets/{pretrain,tokenized}/$(PROFILE), tokenizer y checkpoints de $(PROFILE)? [y/N] " a; \
	[ "$$a" = "y" ] && rm -rf datasets/pretrain/$(PROFILE) datasets/tokenized/$(PROFILE) \
	  tokenizer/trained/$(PROFILE) checkpoints/$(PROFILE) checkpoints/$(PROFILE)-sft || true

jupyter: ## JupyterLab en el contenedor (http://localhost:8888)
	jupyter lab --ip 0.0.0.0 --no-browser --notebook-dir /app
