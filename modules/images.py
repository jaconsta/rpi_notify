import os
from PIL import ImageFont, Image, ImageDraw
from tempfile import NamedTemporaryFile
import textwrap

from config import PATH_DIR


class TextToImage:
    def __init__(self, txt, font_size=20):
        self.text = textwrap.fill(txt, 70)
        self.background = (255, 255, 255)
        self.font_color = (0, 0, 0)
        self.font = ImageFont.truetype(os.path.join(PATH_DIR, 'resources/expressway_rg.ttf'), font_size)
        self.filename = NamedTemporaryFile(delete=False, suffix=".png")

    def text_size(self):
        """
        Determine text size using a scratch image.
        :return:
        """
        img = Image.new("RGBA", (1, 1))
        draw = ImageDraw.Draw(img)
        return draw.textsize(self.text, self.font)

    def create_image(self):
        """
        Create an image based on the text.
        :return:
        """
        img = Image.new("RGBA", self.text_size(), self.background)
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), self.text, self.font_color, self.font)
        img.save(self.filename)
        self.filename.seek(0)

    def del_image(self):
        """
        Close the file and delete.
        :return:
        """
        self.filename.close()
        os.remove(self.filename.name)
