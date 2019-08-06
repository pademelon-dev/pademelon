"""
Calls related to GIT operations
"""

from __future__ import absolute_import, division, print_function

# {{{ Imports
# System Imports
import os

# External Imports
import git

# Local Imports
# }}}


def get_basedir(dirname):
    """
    Working up from the specified directory find a directory with a .git
    folder
    """
    git_repo = git.Repo(dirname, search_parent_directories=True)
    git_root = git_repo.git.rev_parse("--show-toplevel")
    return git_root


def get_modified(branch):
    """
    Use git to get the list of modified files
    """
    basedir = get_basedir(os.path.abspath(os.getcwd()))
    repo = git.Repo(basedir)
    return _get_modified(repo, basedir, branch)


def _get_modified(repo, basedir, branch):
    """
    Use git to get the list of modified files
    """
    diff_entries = repo.commit(branch).diff('HEAD')
    for change_type in ('A', 'R', 'M'):
        for diff_entry in diff_entries.iter_change_type(change_type):
            fname = diff_entry.b_path
            fpath = os.path.join(basedir, fname)
            if os.path.isfile(fpath):
                yield fname
