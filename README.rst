+++++++++++++++++++
sxtools
+++++++++++++++++++

Methods library for Python (cachedef)

cachedef - Decorator responsible for making a cache of the results of calling a method in accordance with the reported parameters. ::

Installing
==========

For install sxtools, run on terminal: ::

    $ [sudo] cd cachedef
    $ [sudo] python setup.py install

Using sxtools
==================

cachedef: 

Decorator responsible for making a cache of the results of calling a method in accordance with the reported parameters. ::

.. code-block:: 
    from sxtools import cachedef
    import datetime


    @cachedef(seed='foo')
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
    print 'test 4: %d ' % foo(1, 2, ignore_cache=True)
    print 'cost: %s' % str(datetime.datetime.now() - start)

    # it takes three seconds
    start = datetime.datetime.now()
    print 'test 5: %d ' % foo(2, 3)
    print 'cost: %s' % str(datetime.datetime.now() - start)
```

development
===========

* Source hosted at `GitHub <https://github.com/sxslex/sxtools>`_

Pull requests are very welcomed! Make sure your patches are well tested.

running the tests
-----------------

if you are using a virtualenv, all you need is:

::

    $ make test

