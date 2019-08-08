"""
Test Utilities
"""
from __future__ import absolute_import, division, print_function

import collections
import io
import os
import shutil
import tempfile
from contextlib import contextmanager

FakeGit = collections.namedtuple("FakeGit", ["repo", "tmpdir", "upstream_branch"])


def add_commit(repo, basedir, paths):
    """
    Utility to add a bunch of file path changes in a git commit.
    """
    for path, data in paths.items():
        dirname = os.path.dirname(path)
        if dirname:
            dirpath = os.path.join(basedir, dirname)
            if not os.path.isdir(dirpath):
                os.makedirs(dirpath)
        fpath = os.path.join(basedir, path)
        with io.open(fpath, "w", encoding="utf-8") as fobj:
            fobj.write(data)
        repo.index.add([path])
    repo.index.commit("An update")


@contextmanager
def git_repo(paths, initial=None):
    """
    Create a test repository.
    """
    import git

    if initial is None:
        initial = {"a.txt": u""}
    upstream_branch = "start"
    origdir = os.getcwd()
    tmpdir = tempfile.mkdtemp()
    try:
        repo = git.Repo.init(tmpdir)
        add_commit(repo, tmpdir, initial)
        fname = "a.txt"
        fpath = os.path.join(tmpdir, fname)
        with io.open(fpath, "w", encoding="utf-8") as fobj:
            fobj.write(u"Test\n")
        repo.index.add([fname])
        repo.index.commit("Empty")
        repo.create_tag(upstream_branch)
        add_commit(repo, tmpdir, paths)
        os.chdir(tmpdir)
        yield FakeGit(repo=repo, tmpdir=tmpdir, upstream_branch=upstream_branch)
    finally:
        os.chdir(origdir)
        shutil.rmtree(tmpdir, ignore_errors=True)
