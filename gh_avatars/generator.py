import hashlib
from random import choice
from PIL import Image, ImageDraw
import numpy as np
import string
from math import ceil

class Avatar:
    """
    Base avatar class
    """

    def __init__(self, size: int = 120, resolution: int = 12, background: str = '#f2f1f2') -> None:
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
        hash_function = hashlib.md5
        hash_obj = hash_function(nick.encode('utf-8'))
        _bytes = hash_obj.digest()

        # Getting binary string 
        half_resolution = ceil(self.resolution / 2)

        binary_str = bin(int(hash_function(nick.encode('utf-8')).hexdigest(), 16))[2:]

        # Extending binary string until length is sufficient for half matrix
        while len(binary_str) < self.resolution * half_resolution:
            hash_obj = hash_function(hash_obj.hexdigest().encode('utf-8'))
            binary_str += bin(int(hash_obj.hexdigest(), 16))[2:]

        # Getting the color from bytes and converting the color to RGB
        if not color:
            color = tuple(channel // 2 + 128 for channel in _bytes[-3:])

        """Generating a matrix of filling blocks"""

        # Generating randomised half grid matrix
        _pattern = np.array(
            [bit == '1' for bit in binary_str[:self.resolution * half_resolution]]
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
        block_size = self.size / self.resolution  # Square size

        img = Image.new('RGB', img_size, self.background)
        draw = ImageDraw.Draw(img)

        for x in range(self.size):
            for y in range(self.size):
                need_to_paint = _pattern[int(x // block_size), int(y // block_size)]
                if need_to_paint:
                    draw.point((x, y), color)

        return img
