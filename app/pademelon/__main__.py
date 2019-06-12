"""
Module load handler for execution via python -m pademelon.

Usage:
    %(exename)s [options] [<args>...]
    %(exename)s (-h | --help)

Options:
    -h --help         Show this screen
    -m <module>       Import and run specified module like python -m

"""
from __future__ import (
    absolute_import, print_function, division, unicode_literals,
)


# {{{ Imports
# System Imports
import sys
import runpy
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
    if args['-m']:
        log_module_run(args['-m'], args)
    else:
        print('Unknown options: %r' % (args,))


def log_module_run(modulename, args):
    """
    Load and run the module like python -m with log dump enabled.
    """
    oldargs = list(sys.argv)
    sys.argv = [modulename] + args['<args>']
    runpy.run_module(modulename, run_name='__main__', alter_sys=True)
    sys.argv = oldargs


if __name__ == '__main__':
    main()
