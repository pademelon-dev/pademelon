#!/bin/bash

set -euxo pipefail

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "${BASEDIR}"

for PYVER in ${PYTHONVERS} ; do
  cd "${BASEDIR}/pip/${PYVER}"
  "python${PYVER}" -m pip install -r test_requirements.txt
  if [ $(wc -l requirements.txt) -gt 0 ] ; then
      "python${PYVER}" -m pip install -r requirements.txt
  fi
  # Display installation
  "python${PYVER}" -m pip freeze
done
