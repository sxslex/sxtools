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

import os
import unittest
import tempfile
from sxtools import GenericImage


class TestGenericImage(unittest.TestCase):

    def test_geretic_image_base64(self):
        gi = GenericImage(iformat='JPEG')
        self.assertIn(
            'data:image/jpeg;base64,',
            gi.base64()
        )

    def test_geretic_image_create_obj(self):
        fobj = tempfile.NamedTemporaryFile(delete=False, mode='wb')
        gi = GenericImage(iformat='JPEG')
        filename = gi.save(fobj)
        self.assertTrue(os.path.exists(filename))
        os.unlink(filename)

    def test_geretic_image_create_name(self):
        filename = os.path.join(tempfile.gettempdir(), 'file_image.jpg')
        gi = GenericImage(iformat='JPEG')
        gi.save(filename)
        self.assertTrue(os.path.exists(filename))
        os.unlink(filename)

    def test_geretic_image_font_not_exists(self):
        gi = GenericImage(font_family='font_not_exists')
        self.assertRaises(
            Exception,
            gi.base64
        )
