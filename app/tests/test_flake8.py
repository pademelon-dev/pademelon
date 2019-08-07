"""
Test modules for pademelon flake8 checks
"""
from __future__ import absolute_import, division, print_function


def test_flake8_only_modified():
    """
    GIVEN a fake GIT repository where existing files with flake8 issues are
    present and new files were more flake8 issues are present WHEN calling
    main THEN the output only reports the new file issues.
    """
    # Setup
    from pademelon.__main__ import main
    from click.testing import CliRunner
    from .util import git_repo

    fname = "fake.py"
    ofname = "other_fake.py"
    bad = u"""
_ = 1 + 1 # missing double space before hash
"""
    with git_repo({fname: bad}, {".isort.cfg": u"", ofname: bad}) as fake_git:
        runner = CliRunner()
        # Exercise
        fullargs = ["--no-show", "--upstream-branch", fake_git.upstream_branch]
        result = runner.invoke(main, fullargs)
    # Verify
    expected = "fake.py:2:10: E261 at least two spaces before inline comment"
    assert expected in result.output  # noqa: S101 # nosec
    assert len(result.output.splitlines()) == 1  # noqa: S101 # nosec
