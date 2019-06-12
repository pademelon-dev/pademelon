from setuptools import setup, find_packages

setup(
    name='pademelon',
    version='0.1.1dev',
    author='Tim Gates',
    author_email='tim.gates@iress.com',
    license='GPLv3+',
    long_description=(
        'Execute a python module or function and log all'
        ' calls and locals to formats that can be compared'
        ' for execution variations.'
    ),
    url='https://github.com/pademelon-dev/pademelon',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
