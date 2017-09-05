# -*- coding: utf-8 -*-

from setuptools import setup
from sxtools import name
from sxtools import __description__
from sxtools import __version__


setup(
    name=name,
    version=__version__,
    url='https://github.com/sxslex/sxtools',
    download_url=(
        'https://github.com/sxslex/sxtools/archive/v1.0.tar.gz'
    ),
    author='Alexandre Villela (SleX)',
    author_email='sx.slex@gmail.com',
    description=__description__,
    keywords=[
        'remove', 'accents',
        'pluralize',
        'join_plus',
        'deep', 'encode', 'decode',
        'capitalize'
    ],
    packages=['sxtools'],
    install_requires=['capitalize-name'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'console_scripts': [
            'sxtools = sxtools.cli:cli',
        ],
    },
)
