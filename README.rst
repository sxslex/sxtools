======
sxtools
======

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/sxslex/sxtools
   :target: https://gitter.im/sxslex/sxtools?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. image:: https://travis-ci.org/sxslex/sxtools.svg?branch=master
    :target: https://travis-ci.org/sxslex/sxtools


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


- SqliteSingle:

.. code-block:: python

    from sxtools import SqliteSingle

    if os.path.exists('students.db'):
        os.unlink('students.db')
    students = SqliteSingle(
        'students.db',
        '''
           create table students (
               id_students          integer primary key,
               name                 varchar(100),
               salary               float,
               birthdate            date
           );
           create table assessments (
               id_assessments       integer primary key,
               id_students          integer,
               grade                float
           );
        '''
    )
    print students.insert(
        'students',
        values=dict(id_students=1, name='slex', salary=3500.10)
    )
    print students.insert(
        'students',
        values=dict(id_students=2, name='denis', salary=8000.50)
    )
    print students.select(
        'students',
        [dict(f='id_students', v=2)]
    )


development
--------

* Source hosted at `GitHub <https://github.com/sxslex/sxtools>`_

Pull requests are very welcomed! Make sure your patches are well tested.

Running the tests
--------

Install dev_requirements.txt `pip install -r requirements.txt`

All you need is:

::

    $ nosetests -dsv --with-yanc --with-coverage --cover-package . tests/test_*.py

