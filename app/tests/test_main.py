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
    import mock
    fake_docopt = mock.patch(
        'pademelon.__main__.docopt', return_value={}
    )
    with fake_docopt:
        # Exercise
        result = main()  # pylint: disable=assignment-from-no-return
    # Verify
    assert result is None  # nosec


def test_show_modified():
    """
    GIVEN the pademelon.__main__ module entry point WHEN calling main with the
    --show-modified flag THEN the call executes successfully with a result of
    `None`
    """
    # Setup
    from pademelon.__main__ import main
    import mock
    fake_docopt = mock.patch(
        'pademelon.__main__.docopt', return_value={
            '--show-modified': 'origin/main',
        }
    )
    fake_get_modified = mock.patch(
        'pademelon.git._get_modified', return_value=[
            'fake.txt',
        ]
    )
    with fake_docopt, fake_get_modified:
        # Exercise
        result = main()  # pylint: disable=assignment-from-no-return
    # Verify
    assert result is None  # nosec
