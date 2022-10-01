#!/bin/bash

set -e
set -X

if [ -d .venv ];then
  /bin/rm -fR .oldvenv
  mv .venv .oldvenv
fi
python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
# https://stackoverflow.com/questions/65122957/resolving-new-pip-backtracking-runtime-issue
# currently the cdk libraries installation has issues ==> use the use-deprecatd flag
pip install --use-deprecated=legacy-resolver -r requirements.txt
pip install -r requirements-dev.txt
pip freeze > pinned_requirements.txt

