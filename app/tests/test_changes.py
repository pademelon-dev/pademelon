"""
Test modules for pademelon.changes
"""
from __future__ import absolute_import, division, print_function

import shutil
import tempfile

import pytest


def test_no_get():
    """
    Ensure an error is raised when not in a git directory
    """
    from pademelon.changes import get_basedir

    tmpdir = tempfile.mkdtemp()
    try:
        with pytest.raises(Exception):
            get_basedir(tmpdir)
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def test_get_modified():
    """
    GIVEN a fake git method WHEN calling the pademelon.changes._get_modified
    method THEN the call returns the fake series of files as modified.
    """
    # Setup
    from pademelon.changes import _get_modified
    from .util import git_repo

    fname = "fakedir/test.txt"
    with git_repo({fname: u""}) as fakegit:
        # Exercise
        result = list(
            _get_modified(fakegit.repo, fakegit.tmpdir, fakegit.upstream_branch)
        )
    # Verify
    assert result == [fname]  # nosec
