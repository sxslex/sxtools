# -*- encoding: utf-8 -*-

import unittest
from sxtools.generic_image import GenericImage


class TestGenericImage(unittest.TestCase):

    def test_geretic_image_crate(self):
        gi = GenericImage(iformat='JPEG')
        self.assertIn(
            'data:image/jpeg;base64,',
            gi.base64()
        )
