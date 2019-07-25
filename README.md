# pademelon

[![Travis Status](https://travis-ci.org/pademelon-dev/pademelon.svg?branch=master)](https://travis-ci.org/pademelon-dev/pademelon)
[![Azure Status](https://dev.azure.com/timgates/timgates/_apis/build/status/pademelon-dev.pademelon?branchName=master)](https://dev.azure.com/timgates/timgates/_build/latest?definitionId=7&branchName=master)
[![PyPi version](https://img.shields.io/pypi/v/pademelon.svg)](https://pypi.org/project/pademelon)
[![Python Versions](https://img.shields.io/pypi/pyversions/pademelon.svg)](https://pypi.org/project/pademelon)
[![PyPi downloads per month](https://img.shields.io/pypi/dm/pademelon.svg)](https://pypi.org/project/pademelon)
[![Documentation Status](https://readthedocs.org/projects/pademelon/badge/?version=latest)](https://pademelon.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/pademelon-dev/pademelon/badge.svg)](https://coveralls.io/github/pademelon-dev/pademelon/)

Used to retrospectively add static type checking on legacy project by just
running the checks on only files modified in a pull request. Can be used as a
soft touch approach to bringing a new checking tool into a large project
without one big bang.

Supported checks include:
* `isort`
* `bandit`
* `flake8`
* `pytest` minimum coverage percentage.
* `pyspelling`

# Available from PyPi.org

https://pypi.org/project/pademelon/

# Install

This library can be installed in (Python)[https://www.python.org/] via
(Pip)[https://pypi.org/].

> pip install pademelon

# Additional Documentation:

* [Online Documentation](https://pademelon.readthedocs.io/en/latest/)
* [News](NEWS.rst).
* [Template Updates](COOKIECUTTER_UPDATES.md).
* [Code of Conduct](CODE_OF_CONDUCT.md).
* [Contribution Guidelines](CONTRIBUTING.md).
