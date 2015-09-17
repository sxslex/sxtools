# -*- encoding: utf-8 -*-

import unittest
from sxtools import string_utils


class TestStringUtils(unittest.TestCase):

    def test_capitalize_name_1(self):
        self.assertEqual(
            string_utils.capitalize_name(u'BRASÍLIA'),
            u'Brasília'
        )

    # def test_to_unicode_1(self):
    #     self.assertEqual(
    #         string_utils.to_unicode('BRAS\xc3\x8dLIA/PLANO PILOTO'),
    #         u'BRASÍLIA/PLANO PILOTO'
    #     )
