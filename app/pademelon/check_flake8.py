"""
Run flake8 checks on modified files
"""

from flake8.main import application


def check_flake8(paths):
    """
    Run flake8 on other files
    """
    app = application.Application()
    app.run(paths)
    app.exit()
