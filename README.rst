======
sxtools
======

The ``sxtools`` Set of libraries to facilitate the work

.. cache_def:: Decorator responsible for making a cache of the results of calling a method in accordance with the reported
.. GenericImage:: Lets you create a generic image to use in development servers
.. string_utils:: Functions to work with packets strings


Installing
--------

For install sxtools, run on terminal: ::

    $ [sudo] cd sxtools
    $ [sudo] python setup.py install

Using sxtools
--------

- cache_def:

.. code-block:: python

    from sxtools import cache_def
    import datetime


    @cache_def(seed='foo')
    def foo(a, b):
        import time
        time.sleep(3)
        return a + b

    start = datetime.datetime.now()

    # it takes three seconds
    print 'test 1: %d ' % foo(1, 2)
    print 'cost: %s' % str(datetime.datetime.now() - start)

    # should return quickly
    start = datetime.datetime.now()
    print 'test 2: %d ' % foo(1, 2)
    print 'cost: %s' % str(datetime.datetime.now() - start)

    start = datetime.datetime.now()
    print 'test 3: %d ' % foo(1, 2)
    print 'cost: %s' % str(datetime.datetime.now() - start)

    # ignore cache
    start = datetime.datetime.now()
    print 'test 4: %d ' % foo(1, 2, renew_cache=True)
    print 'cost: %s' % str(datetime.datetime.now() - start)

    # it takes three seconds
    start = datetime.datetime.now()
    print 'test 5: %d ' % foo(2, 3)
    print 'cost: %s' % str(datetime.datetime.now() - start)


- GenericImage:

.. code-block:: python

    from sxtools import GenericImage

    gi = GenericImage(
        text='image-default',
        width=300,
        height=200
    )
    gi.save('/tmp/image-default.jpg')


- string_utils:

.. code-block:: python

    from sxtools import string_utils

    string_utils.capitalize_name(u'BRASÍLIA/PLANO PILOTO')
    >>> u'Brasília/Plano Piloto'

    string_utils.capitalize_name(u'joão paulo ii')
    >>> u'João Paulo II'

    string_utils.to_unicode('BRASILIA/PLANO PILOTO'),
    >>> u'BRASILIA/PLANO PILOTO'

    string_utils.to_unicode(
        ['BRASILIA/PLANO PILOTO', 1, True, 'Bolas']
    )
    >>> [u'BRASILIA/PLANO PILOTO', 1, True, u'Bolas']


development
--------

* Source hosted at `GitHub <https://github.com/sxslex/sxtools>`_

Pull requests are very welcomed! Make sure your patches are well tested.

Running the tests
--------

Install dev_requirements.txt `pip install -r dev_requirements.txt`

All you need is:

::

    $ make test

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/sxslex/sxtools
   :target: https://gitter.im/sxslex/sxtools?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

