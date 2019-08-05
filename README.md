# pademelon

[![Azure Status](https://dev.azure.com/timgates/timgates/_apis/build/status/pademelon-dev.pademelon?branchName=master)](https://dev.azure.com/timgates/timgates/_build/latest?definitionId=7&branchName=master)
[![Travis Status](https://travis-ci.org/pademelon-dev/pademelon.svg?branch=master)](https://travis-ci.org/pademelon-dev/pademelon)
[![Appveyor Status](https://ci.appveyor.com/api/projects/status/dw6hnqrrdk7ktaw6?svg=true)](https://ci.appveyor.com/project/timgates42/pademelon)
[![PyPI version](https://img.shields.io/pypi/v/pademelon.svg)](https://pypi.org/project/pademelon)
[![Python Versions](https://img.shields.io/pypi/pyversions/pademelon.svg)](https://pypi.org/project/pademelon)
[![PyPI downloads per month](https://img.shields.io/pypi/dm/pademelon.svg)](https://pypi.org/project/pademelon)
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

More details can be found in the
[Online Documentation.](https://pademelon.readthedocs.io/en/latest/)

# Installation

You can install pademelon for
[Python](https://www.python.org/) via
[pip](https://pypi.org/project/pip/)
from [PyPI](https://pypi.org/).

```
$ pip install pademelon
```




## Prerequisites:
- click
- GitPython


## Download from PyPI.org

https://pypi.org/project/pademelon/



# Contributing

Contributions are very welcome, consider using the
[file an issue](https://github.com/pademelon-dev/pademelon/issues)
to discuss the work before beginning, but if you already have a Pull Request
ready then this is no problem, please submit it and it will be very gratefully
considered. The [Contribution Guidelines](CONTRIBUTING.md)
outlines the pademelon commitment to ensuring all
contributions receive appropriate recognition.

# License


Distributed under the terms of the [GPLv3](https://opensource.org/licenses/GPL-3.0)
license, "pademelon" is free and open source software


# Issues

If you encounter any problems, please
[file an issue](https://github.com/pademelon-dev/pademelon/issues)
along with a detailed description.

# Additional Documentation:

* [Online Documentation](https://pademelon.readthedocs.io/en/latest/)
* [News](NEWS.rst).
* [Template Updates](COOKIECUTTER_UPDATES.md).
* [Code of Conduct](CODE_OF_CONDUCT.md).
* [Contribution Guidelines](CONTRIBUTING.md).
