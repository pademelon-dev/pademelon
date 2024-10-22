"""
Test modules for pademelon __main__
"""
from __future__ import absolute_import, division, print_function

import pytest


@pytest.mark.parametrize("args,", [(), ("check",)])
def test_main(args):
    """
    GIVEN the pademelon.__main__ module entry point WHEN calling main THEN
    the call executes successfully with expected output
    """
    # Setup
    from pademelon.__main__ import main
    from click.testing import CliRunner
    from .util import git_repo

    fname = "fake.txt"
    with git_repo({fname: u""}) as fake_git:
        runner = CliRunner()
        # Exercise
        fullargs = list(args) + ["--upstream-branch", fake_git.upstream_branch]
        result = runner.invoke(main, fullargs)
    # Verify
    assert result.output == "%s\n" % (fname,)  # noqa: S101 # nosec
