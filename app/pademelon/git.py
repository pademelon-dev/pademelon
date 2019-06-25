"""
Calls related to GIT operations
"""

from __future__ import (
    absolute_import, print_function, division, unicode_literals,
)


# {{{ Imports
# System Imports
import os
# External Imports
import plumbum
# Local Imports
# }}}


def show_modified(branch):
    """
    Display the list of modified files against target branch
    """
    print('\n'.join(get_modified(branch)))


def get_modified(branch):
    """
    Use git to get the list of modified files
    """
    git = plumbum.local['git']
    return _get_modified(git, branch)


def _get_modified(git, branch):
    """
    Use git to get the list of modified files
    """
    basedir = git('rev-parse', '--show-toplevel').rstrip('\r\n')
    file_list = git('diff', '--name-only', 'HEAD..%s' % (branch,))
    for fname in file_list.splitlines():
        if not fname.strip():
            continue
        fpath = os.path.join(basedir, fname)
        if os.path.isfile(fpath):
            yield fname
