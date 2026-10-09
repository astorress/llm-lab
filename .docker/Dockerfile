######## BASE IMAGE ########
# Mismo patrón que repositorio/data-science: Python copiado sobre Node (Claude
# Code), usuario no-root, historial de bash persistente.
FROM python:3.12-slim-bookworm AS python-base
FROM node:24-bookworm-slim AS img-base

# Arguments
ARG USER=llm
ARG USER_HOME=/home/$USER
ARG VOLUME=/app
ARG SHELL=/bin/bash

COPY --from=python-base /usr/local/ /usr/local/
RUN ldconfig
RUN pip3 install --upgrade pip

RUN apt-get update

# Inital OS configuration
RUN apt-get install -y locales \
    && sed -i 's/^# *\(en_US.UTF-8\)/\1/' /etc/locale.gen \
    && locale-gen
RUN apt-get install -y sudo lsb-release git git-lfs curl zip unzip jq less build-essential
ENV LANG=en_US.UTF-8 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1

# Install Claude Code
RUN npm install -g @anthropic-ai/claude-code \
    && claude --version

# Set up non root user
RUN echo "$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN useradd -ms $SHELL $USER
RUN mkdir -p $VOLUME \
    && chown -R $USER:$USER $VOLUME

# Preserve bash history
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
    && echo $SNIPPET >> "/root/.bashrc" \
    && mkdir /commandhistory \
    && touch /commandhistory/.bash_history \
    && chown -R $USER /commandhistory \
    && echo $SNIPPET >> "$USER_HOME/.bashrc"

# Caché de Hugging Face fuera del repo (volumen nombrado en compose)
ENV HF_HOME=/hf-cache
RUN mkdir -p /hf-cache && chown -R $USER:$USER /hf-cache

# Let non-root user self-update global npm packages (claude-code) at runtime
RUN chown -R $USER:$USER /usr/local/lib/node_modules /usr/local/bin

# Dev utilities shared by every target
RUN pip3 install pytest ruff jupyterlab ipywidgets nbformat


######## DEV IMAGE (CPU) ########
# Devcontainer en Mac: preparación de datos, tokenizador, tests y smoke
# training del perfil tiny. Docker en macOS no expone la GPU (ni MPS), así que
# torch se instala desde el índice CPU (más liviano).
FROM img-base AS img-dev

# Extras pesados de los notebooks 00–08 (bertopic, umap/numba, gensim,
# bert-score…: varios GB). Por defecto NO se instalan; activarlos con
#   WITH_NOTEBOOKS=true en .docker/docker-compose.yml (build.args)
ARG WITH_NOTEBOOKS=false
RUN pip3 install torch --index-url https://download.pytorch.org/whl/cpu
COPY requirements.txt requirements-notebooks.txt /tmp/llm/
RUN if [ "$WITH_NOTEBOOKS" = "true" ]; then \
        pip3 install -r /tmp/llm/requirements-notebooks.txt; \
    else \
        pip3 install -r /tmp/llm/requirements.txt; \
    fi

USER $USER


######## GPU IMAGE (CUDA) ########
# Para cualquier host NVIDIA (RunPod, Vast.ai, Lambda, servidor propio). Las
# wheels de torch en PyPI (linux x86_64) ya traen CUDA/cuDNN; el driver lo pone
# el host vía nvidia-container-toolkit.
# El código y los datos llegan en el bundle (make bundle) — ver docs/06.
FROM img-base AS img-gpu

COPY requirements.txt /tmp/llm/
RUN pip3 install -r /tmp/llm/requirements.txt

USER $USER
WORKDIR /app
ENV PYTHONPATH=/app/src
CMD ["sleep", "infinity"]
