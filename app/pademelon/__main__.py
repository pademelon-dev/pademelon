#!/usr/bin/env python
"""
Module load handler for execution via python -m pademelon.
"""
from __future__ import absolute_import, division, print_function

import click

from pademelon.changes import show_modified
from pademelon.version import __version__

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.version_option(version=__version__)
@click.pass_context
def main(ctxt):
    """
    Run CI checks only against modified files.
    """
    if ctxt.invoked_subcommand is None:
        run_check()


@main.command()
def check(**kwargs):  # pylint: disable=unused-argument
    """
    Run the pademelon check
    """
    run_check()


def run_check():
    """
    Handle pademelon check
    """
    show_modified('start')


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
