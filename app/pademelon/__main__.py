#!/usr/bin/env python
"""
Module load handler for execution via python -m pademelon.
"""
from __future__ import absolute_import, division, print_function

import click

from pademelon.changes import get_modified
from pademelon.version import __version__

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.version_option(version=__version__)
@click.option('--upstream-branch', default='origin/master')
@click.option('--show/--no-show', default=True)
@click.pass_context
def main(ctxt, upstream_branch, show):
    """
    Run CI checks only against modified files.
    """
    if ctxt.invoked_subcommand is None:
        run_check(upstream_branch, show)


@main.command()
@click.option('--upstream-branch', default='origin/master')
@click.option('--show/--no-show', default=True)
def check(upstream_branch, show):  # pylint: disable=unused-argument
    """
    Run the pademelon check
    """
    run_check(upstream_branch, show)


def run_check(upstream_branch, show):
    """
    Handle pademelon check
    """
    file_list = get_modified(upstream_branch)
    if show:
        print('\n'.join(file_list))


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
