#!/bin/bash

COLOR_GREEN=$(tput setaf 2)
COLOR_BLUE=$(tput setaf 4)
COLOR_MAGENTA=$(tput setaf 5)
COLOR_DEFAULT=$(tput sgr0)

EXEC_PATH=$(dirname $(readlink -f "$0"))
HOME_PATH=$EXEC_PATH/..
STEP=1
STEP_COUNT=3

echo "${COLOR_MAGENTA}${STEP}/$STEP_COUNT:${COLOR_GREEN} Configuring Git.${COLOR_DEFAULT}"
GIT_SCRIPT_PATH=$EXEC_PATH/git.sh
chmod +x $GIT_SCRIPT_PATH
. $GIT_SCRIPT_PATH
let STEP++

cd $HOME_PATH
echo "${COLOR_MAGENTA}${STEP}/$STEP_COUNT:${COLOR_GREEN} Installing ${COLOR_BLUE}llm-lab${COLOR_GREEN} in editable mode.${COLOR_DEFAULT}"
pip3 install --user --no-deps -e . > /dev/null && echo "INFO: llm_lab importable"
let STEP++

echo "${COLOR_MAGENTA}${STEP}/$STEP_COUNT:${COLOR_GREEN} Checking environment.${COLOR_DEFAULT}"
python3 -c "import torch, tokenizers, datasets; print(f'INFO: torch {torch.__version__} | tokenizers {tokenizers.__version__} | datasets {datasets.__version__}')"
if [ -d /personal ]; then
    echo "INFO: Personal corpus root mounted at /personal (read-only)"
fi
if [ -z "$HF_TOKEN" ]; then
    echo "WARNING: HF_TOKEN empty in .envs/hf.env (public datasets still work, with lower rate limits)."
fi

echo "$COLOR_DEFAULT"
