#!/bin/python
"""Goes through a directory of landscape oriented images and resizes
them so that the width is 1920px without losing the orignal ratio"""

from PIL import Image, UnidentifiedImageError
import os
from tqdm import tqdm


def get_new_dimensions(image):
    """Resize the image so the width dimension is 1920px"""
    scale = 1920 / image.size[0]
    new_width = int(image.size[0] * scale)
    new_height = int(image.size[1] * scale)

    return new_width, new_height


if __name__ == '__main__':

    for file in tqdm(os.listdir(os.getcwd())):
        try:
            image = Image.open(file)
        except IsADirectoryError:
            print("(Skipping) '%s' is a directory." % file)
        except UnidentifiedImageError:
            print("(Skipping) '%s' is not an image." % file)
        else:
            new_image = image.resize(get_new_dimensions(image))
            new_image.save(file)
            image.close()