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

import unittest
from sxtools import string_utils


class TestStringUtils(unittest.TestCase):

    def test_capitalize_name_1(self):
        self.assertEqual(
            string_utils.capitalize_name(u'BRASÍLIA'),
            u'Brasília'
        )

    def test_capitalize_name_2(self):
        self.assertEqual(
            string_utils.capitalize_name(u'BRASÍLIA/PLANO PILOTO'),
            u'Brasília/Plano Piloto'
        )

    def test_capitalize_name_3(self):
        self.assertEqual(
            string_utils.capitalize_name(u'joão paulo ii'),
            u'João Paulo II'
        )

    def test_capitalize_name_4(self):
        self.assertEqual(
            string_utils.capitalize_name(''),
            u''
        )

    def test_to_unicode_str(self):
        self.assertEqual(
            string_utils.to_unicode('BRASILIA/PLANO PILOTO'),
            u'BRASILIA/PLANO PILOTO'
        )

    def test_to_unicode_list(self):
        self.assertListEqual(
            string_utils.to_unicode(
                ['BRASILIA/PLANO PILOTO', 1, True, 'Bolas']
            ),
            [u'BRASILIA/PLANO PILOTO', 1, True, u'Bolas']
        )

    def test_to_unicode_dict(self):
        self.assertDictEqual(
            string_utils.to_unicode(
                dict(name='BRASILIA/PLANO PILOTO', idade=1, sport='Tenis')
            ),
            dict(name=u'BRASILIA/PLANO PILOTO', idade=1, sport=u'Tenis')
        )

    def test_to_unicode_latin(self):
        self.assertEquals(
            string_utils.to_unicode(
                'Ol\xe1'
            ),
            u'Olá'
        )
