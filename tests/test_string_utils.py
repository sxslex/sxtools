# -*- encoding: utf-8 -*-

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
