#!/bin/python
"""Finds all landscape oriented images in the current working directory
and copies them into a subdirectory"""

from PIL import Image
import os, shutil


if not os.path.exists('papers'):
    os.mkdir('papers')

for item in os.listdir(os.getcwd()):
    try:
        image = Image.open(item)
    except:
        print('Not an image: %s' % item)
        continue
    else:
        if image.size[0] > image.size[1]:
            shutil.copy(item, 'papers/')