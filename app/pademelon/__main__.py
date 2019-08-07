#!/usr/bin/env python
"""
Module load handler for execution via python -m pademelon.
"""
from __future__ import absolute_import, division, print_function

import os

import click

from pademelon.changes import get_basedir, get_modified
from pademelon.check_flake8 import check_flake8
from pademelon.version import __version__

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.version_option(version=__version__)
@click.option('--upstream-branch', default='origin/master')
@click.option('--show/--no-show', default=True)
@click.option('--flake8/--no-flake8', default=True)
@click.pass_context
def main(ctxt, upstream_branch, show, flake8):
    """
    Run CI checks only against modified files.
    """
    if ctxt.invoked_subcommand is None:
        run_check(upstream_branch, show, flake8)


@main.command()
@click.option('--upstream-branch', default='origin/master')
@click.option('--show/--no-show', default=True)
@click.option('--flake8/--no-flake8', default=True)
def check(upstream_branch, show, flake8):  # pylint: disable=unused-argument
    """
    Run the pademelon check
    """
    run_check(upstream_branch, show, flake8)


def run_check(upstream_branch, show, flake8):
    """
    Handle pademelon check
    """
    file_list = list(get_modified(upstream_branch))
    basedir = get_basedir(os.getcwd())
    file_py = [
        os.path.join(basedir, filename) for filename in file_list
        if os.path.splitext(filename)[-1] == '.py'
    ]
    if show:
        print('\n'.join(file_list))
    if flake8:
        check_flake8(file_py)


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
