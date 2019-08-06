"""
Test modules for pademelon __main__
"""

import pytest


@pytest.mark.parametrize('args', [
    ([],),
    (['check'],),
])
def test_main(args):
    """
    GIVEN the pademelon.__main__ module entry point WHEN calling main THEN
    the call executes successfully with expected output
    """
    # Setup
    from pademelon.__main__ import main
    from click.testing import CliRunner
    import mock
    fake_get_modified = mock.patch(
        'pademelon.changes._get_modified', return_value=[
            'fake.txt',
        ]
    )
    runner = CliRunner()
    with fake_get_modified:
        # Exercise
        result = runner.invoke(main, args)
    # Verify
    assert result.output == 'fake.txt\n'  # nosec
