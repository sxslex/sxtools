# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='sxtools',
    version='1.0.1',
    description=(
        'Useful Functions Set: Remove Accents, Pluralize, Deep Encode and etc..'
    ),
    url='https://github.com/sxslex/sxtools',
    download_url=(
        'https://github.com/sxslex/sxtools/archive/v1.0.1.tar.gz'
    ),
    author='Alexandre Villela (SleX)',
    author_email='sx.slex@gmail.com',
    keywords=[
        'remove', 'accents',
        'pluralize',
        'join_plus',
        'deep', 'encode', 'decode',
        'capitalize'
    ],
    packages=['sxtools'],
    install_requires=['capitalize-name', 'click'],
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
