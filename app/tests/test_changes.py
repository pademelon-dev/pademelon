"""
Test modules for pademelon.changes
"""


import io
import os
import tempfile


def test_get_modified():
    """
    GIVEN a fake git method WHEN calling the pademelon.changes._get_modified
    method THEN the call returns the fake series of files as modified.
    """
    # Setup
    from pademelon.changes import _get_modified
    import git
    tmpdir = tempfile.mkdtemp()
    repo = git.Repo.init(tmpdir)
    repo.index.commit('Empty')
    repo.create_tag('start')
    fname = 'test.txt'
    fpath = os.path.join(tmpdir, fname)
    with io.open(fpath, 'wb'):
        pass
    repo.index.add([fname])
    repo.index.commit('An update')
    # Exercise
    result = _get_modified(repo, tmpdir, 'start')
    # Verify
    assert list(result) == [fname]  # nosec
