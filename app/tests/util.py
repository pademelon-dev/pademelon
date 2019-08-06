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

FakeGit = collections.namedtuple(
    'FakeGit', [
        'repo', 'tmpdir', 'upstream_branch'
    ]
)


@contextmanager
def git_repo(paths):
    """
    Create a test repository.
    """
    import git
    upstream_branch = 'start'
    origdir = os.getcwd()
    tmpdir = tempfile.mkdtemp()
    try:
        repo = git.Repo.init(tmpdir)
        fname = 'a.txt'
        fpath = os.path.join(tmpdir, fname)
        with io.open(fpath, 'w', encoding='utf-8') as fobj:
            fobj.write(u'Test\n')
        repo.index.add([fname])
        repo.index.commit('Empty')
        repo.create_tag(upstream_branch)
        for path, data in paths.items():
            dirname = os.path.dirname(path)
            if dirname:
                dirpath = os.path.join(tmpdir, dirname)
                if not os.path.isdir(dirpath):
                    os.makedirs(dirpath)
            fpath = os.path.join(tmpdir, path)
            with io.open(fpath, 'w', encoding='utf-8') as fobj:
                fobj.write(data)
            repo.index.add([path])
        repo.index.commit('An update')
        os.chdir(tmpdir)
        yield FakeGit(
            repo=repo, tmpdir=tmpdir, upstream_branch=upstream_branch,
        )
    finally:
        os.chdir(origdir)
        shutil.rmtree(tmpdir, ignore_errors=True)
