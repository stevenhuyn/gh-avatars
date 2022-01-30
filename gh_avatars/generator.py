import hashlib
from random import choice
from PIL import Image, ImageDraw
import numpy as np
import string


class Avatar:
    """
    Base avatar class
    """

    def __init__(self, size: int = 120, resolution: int = 6, background: str = '#f2f1f2',) -> None:
        """
        Avatar init

        :param background: str background color (#f2f1f2)
        :param resolution: int size of width of pixel grid to generate
        :param size: int avatar size multiple of (resolution)
        :return: None
        """
        self.background = background
        self.resolution = resolution 
        self.size = size

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
        _bytes = hashlib.sha512(nick.encode('utf-8')).digest()

        # Getting binary string
        _binary_str = bin(int(hashlib.sha512(nick.encode('utf-8')).hexdigest(), 16))[2:]

        # Getting the color from bytes and converting the color to RGB
        if not color:
            color = tuple(channel // 2 + 128 for channel in _bytes[-3:])

        """Generating a matrix of filling blocks"""
        half_resolution = (self.resolution // 2) + 1

        # Generating randomised half grid matrix
        _pattern = np.array(
            [bit == '1' for bit in _binary_str[:self.resolution * half_resolution]]
        ).reshape(half_resolution, self.resolution)


        # Mirroring to get full grid
        if self.resolution % 2 == 0:
            # Even sized pattern
            _pattern = np.concatenate((_pattern, _pattern[::-1]), axis=0)
        else:
            # Odd sized pattern
            _pattern = np.concatenate((_pattern, _pattern[::-1][1:]), axis=0)


        # Removing blocks at the edges
        for i in range(self.resolution):
            _pattern[0, i] = 0
            _pattern[self.resolution - 1, i] = 0
            _pattern[i, 0] = 0
            _pattern[i, self.resolution - 1] = 0

        """Draw images according to the filling matrix"""

        img_size = (self.size, self.size)
        block_size = self.size // self.resolution  # Square size

        img = Image.new('RGB', img_size, self.background)
        draw = ImageDraw.Draw(img)

        for x in range(self.size):
            for y in range(self.size):
                need_to_paint = _pattern[x // block_size, y // block_size]
                if need_to_paint:
                    draw.point((x, y), color)

        return img
