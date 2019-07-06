"""
Setuptool Distribution for pademelon
"""

from setuptools import setup

setup(
    name='pademelon',
    version='0.1.2dev',
    author='Tim Gates',
    author_email='tim.gates@iress.com',
    packages=['pademelon'],
    license='GPLv3+',
    long_description=(
        'Used to retrospectively add static type checking on legacy project'
        ' by just running the checks on only files modified in a pull'
        ' request.'
    ),
    url='https://github.com/pademelon-dev/pademelon',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=['docopt', 'plumbum'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE V3 (GPLV3)",
    ],
)
