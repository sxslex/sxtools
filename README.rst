======
sxtools
======

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/sxslex/sxtools
   :target: https://gitter.im/sxslex/sxtools?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. image:: https://img.shields.io/badge/pypi-v1.0-orange.svg
    :target: https://pypi.python.org/pypi/sxtools

.. image:: https://img.shields.io/badge/python-2.6%2C%202.7%2C%203.3+-blue.svg
    :target: https://travis-ci.org/sxslex/sxtools.svg?branch=master

.. image:: https://travis-ci.org/sxslex/sxtools.svg?branch=master
    :target: https://travis-ci.org/sxslex/sxtools

.. image:: https://img.shields.io/badge/license--blue.svg
    :target: https://github.com/sxslex/sxtools/blob/master/LICENSE


The ``sxtools`` Useful Functions Set: Remove Accents, Pluralize, Deep Encode and etc..
Passes all original unittests.


Usage
=====

.. code:: pycon

    >>> import sxtools
    >>> sxtools.join_plus(['Slex', 'Dénis', 'Rafs'], end=' and ')
    'Slex, Dénis and Rafs'

.. code:: pycon

    >>> import sxtools
    >>> sxtools.remove_accents('Olá Mundo')
    'Ola Mundo'


Installation
============

Use ``pip`` or ``easy_install``:

.. code::

    $ pip install sxtools


Development
===========

Use py.test to run unittests
