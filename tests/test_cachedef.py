# -*- encoding: utf-8 -*-

from sxtools import cachedef
import unittest
import datetime
import os


@cachedef(
    # seed so that the cache be saved alone
    seed='foo',
    # directory cache
    path='/tmp' if os.path.exists('c:/') else 'c:/tmp',
    # cache time in minutes
    minuteexpire=15,
    # debug mode
    debug=False
)
def foo(a, b):
    import time
    time.sleep(3)
    return a + b


class CacheDefTestCase(unittest.TestCase):

    def test_cachedef_1(self):
        self.assertEqual(3, foo(1, 2))
        self.assertEqual(3, foo(1, 2))

    def test_cachedef_2(self):
        self.assertEqual(4, foo(1, 3))
        start = datetime.datetime.now()
        self.assertEqual(4, foo(1, 3))
        cost = datetime.datetime.now() - start
        self.assertTrue(
            cost < datetime.timedelta(seconds=2)
        )
        start = datetime.datetime.now()
        self.assertEqual(4, foo(1, 3, ignore_cache=True))
        cost = datetime.datetime.now() - start
        self.assertTrue(
            cost > datetime.timedelta(seconds=2)
        )


if __name__ == '__main__':
    unittest.main()
