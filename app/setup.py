#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setuptool Distribution for pademelon
"""

# {{{ Import
# System  Imports
import codecs
import os

# External Imports
from setuptools import setup

# }}}


def read(fname):
    """
    Read the contents of relative file.
    """
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pademelon',
    version='0.1.2dev',
    author='Tim Gates',
    author_email='tim.gates@iress.com',
    maintainer='Tim Gates',
    maintainer_email='tim.gates@iress.com',
    packages=['pademelon'],
    license='GPLv3+',
    description=(
        'Used to retrospectively add static type checking on legacy project'
        ' by just running the checks on only files modified in a pull'
        ' request.'
    ),
    url='https://github.com/pademelon-dev/pademelon',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=['docopt', 'plumbum'],
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
