"""
Module load handler for execution via python -m pademelon.

Usage:
    %(exename)s [options] [<args>...]
    %(exename)s (-h | --help)

Options:
    -h --help         Show this screen

"""
from __future__ import (
    absolute_import, print_function, division, unicode_literals,
)


# {{{ Imports
# System Imports
import sys
# External Imports
from docopt import docopt
# }}}


def main():
    """
    Main Command Line entry point
    """
    args = docopt(__doc__ % {
        'exename': ''.join(sys.argv[0:1]),
    })
    print('Unknown options: %r' % (args,))


if __name__ == '__main__':
    main()
