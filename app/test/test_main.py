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
    # Exercise
    result = main()  # pylint: disable=assignment-from-no-return
    # Verify
    assert result is None
