# -*- encoding: utf-8 -*-

import unittest
from sxtools.generic_image import GenericImage


class TestGenericImage(unittest.TestCase):

    def test_geretic_image_crate(self):
        gi = GenericImage(iformat='JPEG')
        # gi.save('/tmp/newimage.jpg')
        self.assertIn(
            'data:image/jpeg;base64,' in gi.base64()
        )
