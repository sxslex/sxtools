# -*- coding: utf-8 -*-
#
# Copyright 2015 Alexandre Villela (SleX) <https://github.com/sxslex/sxtools/>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    by sx.slex@gmail.com

from sxtools import cache_def
import unittest
import tempfile
import shutil
import os
foo_executando = False
path_default = os.path.join(tempfile.gettempdir(), 'cache_def')

try:
    if os.path.exists(path_default):
        os.unlink(path_default)
        if os.path.isdir(path_default):
            shutil.rmtree(path_default)
        else:
            os.remove(path_default)
except Exception:
    pass


class TestCacheDef(unittest.TestCase):

    def test_cache_def_basic(self):
        @cache_def(
            # seed so that the cache be saved alone
            seed='foo_basic',
            # directory cache
            path=path_default,
            # cache time in minutes
            minuteexpire=15,
            # debug mode
            debug=True
        )
        def foo(a, b):
            global foo_executando
            foo_executando = True
            return a + b
        self.assertEqual(3, foo(1, 2))
        self.assertEqual(3, foo(1, 2))
        shutil.rmtree(os.path.join(path_default, 'foo_basic'))

    def test_cache_def_literal(self):
        @cache_def(
            seed='foo_literal',
            path=path_default,
            minuteexpire=15,
            debug=False,
            ftype='literal'
        )
        def foo(a, b):
            global foo_executando
            foo_executando = True
            return a + b
        self.assertEqual(3, foo(1, 2))
        self.assertEqual(3, foo(1, 2))
        shutil.rmtree(os.path.join(path_default, 'foo_literal'))

    def test_cache_def_ftype_invalid(self):
        @cache_def(
            seed='ftype_invalid',
            path=path_default,
            minuteexpire=15,
            debug=False,
            ftype='slex'
        )
        def foo(a, b):
            global foo_executando
            foo_executando = True
            return a + b
        f = open(os.path.join(path_default, 'ftype_invalid'), 'w')
        f.write('.')
        f.close()
        self.assertRaises(
            Exception, foo,
            (1, 2)
        )

    def test_cache_def_full(self):
        @cache_def(
            # seed so that the cache be saved alone
            seed='def_full',
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
        self.assertEqual(4, foo(1, 3))
        foo_executando = False
        self.assertEqual(4, foo(1, 3))
        self.assertFalse(foo_executando)
        foo_executando = True
        self.assertEqual(4, foo(1, 3, ignore_cache=True))
        self.assertTrue(foo_executando)
        shutil.rmtree(os.path.join(path_default, 'def_full'))
