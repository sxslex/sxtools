# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# @ame:         genericimage.py
# @description: Lets you create a generic image to use in development servers
# @author:      slex
# @create:      2015-07-06
# @version:     1.0
# -----------------------------------------------------------------------------
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from StringIO import StringIO
PROJECT_APPLICATION_PATH = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = PROJECT_APPLICATION_PATH


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
        font_family=CACHE_PATH + '/fonts/Arialn.ttf'
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
        if not os.path.exists(self.font_family):
            raise Exception('file does not exist: ' + str(self.font_family))
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

    def save(self, filename):
        f = open(filename, 'wb')
        f.write(self.create())
        f.close()
        return True

    def base64(self):
        import base64
        return 'data:image/' + self.iformat.lower() + ';base64,' + \
            base64.b64encode(self.create())


# if __name__ == '__main__':
#     gi = GenericImage(iformat='JPEG')
#     gi.save('/tmp/newimage.jpg')
#     print gi.base64()
