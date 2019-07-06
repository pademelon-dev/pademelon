"""
Module load handler for execution via python -m pademelon.

Usage:
    %(exename)s [options] [<args>...]
    %(exename)s (-h | --help)

Options:
    -h --help                  Show this screen
    --show-modified=<branch>   Display details of the modified files against
                               GIT branch

"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# {{{ Imports
# System Imports
import sys

# External Imports
from docopt import docopt

# Local Imports
from pademelon.git import show_modified

# }}}


def main():
    """
    Main Command Line entry point
    """
    args = docopt(__doc__ % {
        'exename': ''.join(sys.argv[0:1]),
    })
    if args.get('--show-modified') is not None:
        show_modified(args['--show-modified'])
    else:
        print('Unknown options: %r' % (args,))


if __name__ == '__main__':
    main()
