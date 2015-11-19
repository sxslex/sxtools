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

from sxtools.cache_def import _loads
from sxtools.cache_def import _dumps
from sxtools.cache_def import _getcontextfile
from sxtools.cache_def import _setcontextfile
from sxtools import cache_def_clear_expired
from sxtools import cache_def
import unittest
import tempfile
import shutil
import time
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

    def test_00_cache_def_basic(self):
        @cache_def(
            # seed so that the cache be saved alone
            seed='foo_basic',
            # directory cache
            path=path_default,
            # cache time in minutes
            minuteexpire=15,
            # debug mode
            debug=False
        )
        def foo(a, b):
            return a + b
        self.assertEqual(3, foo(1, 2))
        self.assertEqual(3, foo(1, 2))
        shutil.rmtree(path_default)

    def test_01_cache_def_literal(self):
        @cache_def(
            seed='foo_literal',
            path=path_default,
            minuteexpire=15,
            debug=False,
            ftype='literal'
        )
        def foo(a, b):
            return a + b
        self.assertEqual(3, foo(1, 2))
        self.assertEqual(3, foo(1, 2))
        shutil.rmtree(path_default)

    def test_02_cache_def_ftype_invalid(self):
        @cache_def(
            seed='ftype_invalid',
            path=path_default,
            minuteexpire=15,
            debug=False,
            ftype='slex'
        )
        def foo(a, b):
            return a + b
        if not os.path.exists(path_default):
            os.mkdir(path_default, 0777)
        f = open(os.path.join(path_default, 'ftype_invalid'), 'w')
        f.write('.')
        f.close()
        self.assertRaises(
            Exception,
            foo,
            a=1,
            b=2
        )
        shutil.rmtree(path_default)

    def test_03_cache_def_ftype_invalid_loads(self):
        self.assertRaises(
            Exception,
            _loads,
            s='/',
            ftype='slex'
        )

    def test_04_cache_def_ftype_invalid_dumps(self):
        self.assertRaises(
            Exception,
            _dumps,
            s='/',
            ftype='slex'
        )

    def test_05_cache_def_invalid_getcontextfile(self):
        self.assertIsNone(_getcontextfile(pathfile='/tmp_xpto/'))

    def test_06_cache_def_full(self):
        global foo_executando

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
        self.assertEqual(4, foo(1, 3, renew_cache=True))
        self.assertTrue(foo_executando)
        shutil.rmtree(path_default)

    def test_07_getcontextfile_file_corrupt(self):
        if not os.path.exists(path_default):
            os.mkdir(path_default, 0777)
        pathfile = os.path.join(path_default, 'corrupt')
        if os.path.exists(pathfile):
            os.unlink(pathfile)
        _setcontextfile(
            pathfile=pathfile,
            context=dict(a='1'),
            ftype='literal'
        )
        self.assertIsNone(
            _getcontextfile(
                pathfile=pathfile,
                minuteexpire=5,
                debug=False,
                ftype='pickle'
            )
        )
        shutil.rmtree(path_default)

    def test_08_getcontextfile_is_dir(self):
        if os.path.exists(path_default):
            shutil.rmtree(path_default)
        os.mkdir(path_default, 0777)
        pathfile = os.path.join(path_default, 'directore')
        os.mkdir(pathfile, 0777)
        self.assertIsNone(
            _getcontextfile(
                pathfile=pathfile,
                minuteexpire=5,
                debug=False,
                ftype='pickle'
            )
        )
        shutil.rmtree(path_default)

    def test_09_cache_def_expired(self):
        global foo_executando

        @cache_def(
            # seed so that the cache be saved alone
            seed='def_expired',
            # directory cache
            path=path_default,
            # cache time in minutes
            minuteexpire=0,  # menus de 1 segundo
            # debug mode
            debug=False
        )
        def foo(a, b):
            global foo_executando

            foo_executando = True
            return a + b
        foo_executando = False
        self.assertEqual(4, foo(1, 3))
        self.assertTrue(foo_executando)
        time.sleep(0.01)
        foo_executando = False
        self.assertEqual(4, foo(1, 3))
        self.assertTrue(foo_executando)
        shutil.rmtree(path_default)

    def test_10_cache_def_not_path(self):
        @cache_def(
            # seed so that the cache be saved alone
            seed='not_path'
        )
        def foo(a, b):
            return a + b
        self.assertEqual(4, foo(1, 3))

    def test_11_cache_def_db_cache_info(self):
        @cache_def(
            # seed so that the cache be saved alone
            seed='db_cache_info',
            # redis host
            redishost='127.0.0.1',
            # cache time in minutes
            minuteexpire=15,
            # debug mode
            debug=False,
        )
        def foo(a, b):
            time.sleep(0.01)
            return a + b
        self.assertEqual(3, foo(1, 2))
        self.assertEqual(8, foo(4, 4))
        self.assertEqual(8, foo(4, 4))
        self.assertEqual(8, foo(4, 4))
        self.assertEqual(9, foo(5, 4))
        self.assertEqual(3, foo(1, 2, renew_cache=True))
        self.assertEqual(9, foo(5, 4))
        self.assertEqual(9, foo(5, 4))
        self.assertEqual(9, foo(5, 4))
