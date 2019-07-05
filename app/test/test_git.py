"""
Test modules for pademelon.git
"""


import io
import os
import tempfile

import mock


def test_get_modified():
    """
    GIVEN a fake git method WHEN calling the pademelon.git._get_modified
    method THEN the call returns the fake series of files as modified.
    """
    # Setup
    from pademelon.git import _get_modified
    fakegit = mock.Mock()
    tmpdir = tempfile.mkdtemp()
    fname = 'test.txt'
    fpath = os.path.join(tmpdir, fname)
    with io.open(fpath, 'wb'):
        pass
    fakegit.side_effect = [
        tmpdir,
        '{}\n\n'.format(fname),
    ]
    # Exercise
    result = _get_modified(fakegit, 'origin/master')
    # Verify
    assert list(result) == [fname]  # nosec
