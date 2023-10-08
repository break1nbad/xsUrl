#!/usr/bin/env bash
# exit on error
set -o errexit


#virtualenv .env --python=python3.10
#source .env/bin/activate

python -m pip install --upgrade pip setuptools
pip install --upgrade -r requirements.txt

