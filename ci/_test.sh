#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "${THISDIR}" )"
HOSTDIR="${1}"
shift 1

MAIN_MODULE="pademelon"
MODULES=( "${MAIN_MODULE}" "test" )

cd "${BASEDIR}"
python -m pyspelling
cd "${BASEDIR}/app"
python -m flake8 "${MODULES[@]}"
python -m pylint "${MODULES[@]}"
python -m bandit -r "${MAIN_MODULE}"
python -m pytest --path-mapping "${BASEDIR}" "${HOSTDIR}" --cov-report=term --cov-report=html --cov-config=.coveragerc --cov-fail-under=100 "--cov=${MAIN_MODULE}"
python -m pademelon --show-modified origin/master
echo 'Testing Complete'
