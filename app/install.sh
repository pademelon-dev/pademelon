#!/bin/bash

set -euxo pipefail

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "${BASEDIR}"

apt-get update
apt-get install -qq -y aspell aspell-en
apt-get install -qq -y hunspell hunspell-en-au

python -m pip install pipenv
python -m pipenv install --deploy --system 
