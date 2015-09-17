# -*- encoding: utf-8 -*-

from sxtools import cache_def
import unittest
<<<<<<< HEAD:tests/test_cache_def.py
import os

foo_executando = False

=======
import platform

foo_executando = False

path_default = '/tmp'
if platform.system() == 'Windows':
    path_default = 'c:/tmp'

>>>>>>> e58f370963d77c06aefdd3f41d3542d870f30a02:tests/test_cache_def.py

@cache_def(
    # seed so that the cache be saved alone
    seed='foo',
    # directory cache
    path=path_default,
    # cache time in minutes
    minuteexpire=15,
    # debug mode
    debug=False
)
def foo(a, b):
    global foo_executando
    foo_executando = True
    return a + b


class TestCacheDef(unittest.TestCase):

    def test_cachedef_1(self):
        self.assertEqual(3, foo(1, 2))
        self.assertEqual(3, foo(1, 2))

    def test_cachedef_2(self):
        global foo_executando
        self.assertEqual(4, foo(1, 3))
        foo_executando = False
        self.assertEqual(4, foo(1, 3))
        self.assertFalse(foo_executando)
        foo_executando = True
        self.assertEqual(4, foo(1, 3, ignore_cache=True))
        self.assertTrue(foo_executando)
