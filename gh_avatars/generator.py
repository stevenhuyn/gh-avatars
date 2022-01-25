import hashlib
from random import choice
from PIL import Image, ImageDraw
import numpy as np
import string


class Avatar:
    """
    Base avatar class
    """

    def __init__(self, size: int = 120, background: str = '#f2f1f2') -> None:
        """
        Avatar init

        :param size: int avatar size (multiple of 12) [base 120]
        :param background: str background color (#f2f1f2)
        :return: None
        """
        self.size = size
        self.background = background

    def generate(self, nick: str = None, color: str = None) -> Image:
        """
        Avatar generator

        :param nick: str
        :param color: str with hex color for block (#abcabc)
        :return: Image (Pillow obj)
        """

        # Getting random nick if none
        if not nick:
            nick = ''.join(
                [choice(string.ascii_lowercase + string.digits if i != 5 else string.ascii_uppercase) for i in
                 range(6)])

        # Getting bytes from a nickname
        _bytes = hashlib.md5(nick.encode('utf-8')).digest()

        # Getting the color from bytes and converting the color to RGB
        if not color:
            color = tuple(channel // 2 + 128 for channel in _bytes[6:9])

        """Generating a matrix of filling blocks"""
        # 6x12 array
        _pattern = np.array(
            [bit == '1' for byte in _bytes[3:3 + 9] for bit in bin(byte)[2:].zfill(8)]
        ).reshape(6, 12)
        # Increasing to 12x12 array
        _pattern = np.concatenate((_pattern, _pattern[::-1]), axis=0)

        # Removing blocks at the edges
        for i in range(12):
            _pattern[0, i] = 0
            _pattern[11, i] = 0
            _pattern[i, 0] = 0
            _pattern[i, 11] = 0

        """Draw images according to the filling matrix"""

        img_size = (self.size, self.size)
        block_size = self.size // 12  # Square size

        img = Image.new('RGB', img_size, self.background)
        draw = ImageDraw.Draw(img)

        for x in range(self.size):
            for y in range(self.size):
                need_to_paint = _pattern[x // block_size, y // block_size]
                if need_to_paint:
                    draw.point((x, y), color)

        print(nick)
        return img
