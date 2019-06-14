"""
Test modules for pademelon __main__
"""


def test_main():
    """
    GIVEN the pademelon.__main__ module entry point WHEN calling main THEN
    the call executes successfully with a result of `None`
    """
    # Setup
    from pademelon.__main__ import main
    from unittest import mock
    fake_docopt = mock.patch(
        'pademelon.__main__.docopt', return_value={}
    )
    with fake_docopt:
        # Exercise
        result = main()  # pylint: disable=assignment-from-no-return
    # Verify
    assert result is None
