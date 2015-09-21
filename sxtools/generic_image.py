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
# Lets you create a generic image to use in development servers
#    by sx.slex@gmail.com

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from StringIO import StringIO


class GenericImage(object):

    def __init__(
        self,
        text=None,
        width=300,
        height=200,
        iformat='JPEG',
        background_color=(203, 203, 203),
        text_color=(149, 149, 149),
        font_size=24,
        font_family='arial'
    ):
        self.text = text
        self.width = width
        self.height = height
        self.iformat = iformat
        self.font_size = font_size
        self.font_family = font_family
        self.background_color = background_color
        self.text_color = text_color

    def create(self):
        img = Image.new(
            'RGB',
            (self.width, self.height), color=self.background_color
        )
        draw = ImageDraw.Draw(img)
        fontt = ImageFont.truetype(
            self.font_family,
            self.font_size
        )
        if not self.text:
            self.text = '%sx%s' % (str(self.width), str(self.height))
        tz = draw.textsize(self.text, fontt)
        draw.text(
            xy=(
                ((self.width - tz[0]) / 2),
                ((self.height - tz[1]) / 2)
            ),
            text=self.text,
            fill=self.text_color,
            font=fontt
        )
        img2 = StringIO()
        img.save(img2, 'JPEG')
        img2.seek(0)
        return img2.read()

    def save(self, filename_or_fobj):
        if getattr(filename_or_fobj, 'read', None) is not None:
            fobj = filename_or_fobj
        else:
            fobj = open(filename_or_fobj, mode='wb')
        filename = getattr(fobj, 'name', None)
        fobj.write(self.create())
        fobj.close()
        return filename

    def base64(self):
        import base64
        return 'data:image/' + self.iformat.lower() + ';base64,' + \
            base64.b64encode(self.create())
