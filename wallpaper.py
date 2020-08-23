#!/bin/python

"""
wallpape.py: This script checks all of the images in the
requested directory (as long as it exists in the chan scrape
directory). If the images are landscape orientation and at
least 1920 pixels in width then they are moved to a nested
directory called '1920w'. All images in '1920w' are then
checked to see if they are 16:9, moving them to a directory
called '16x9' if they meet the check. Any images in the 16x9
directory with a width that exceeds 1920 will be resized to
1920 x 1080.
"""

from PIL import Image
from os import listdir, mkdir
from os.path import join, isdir
from shutil import move
import sys

if len(sys.argv) == 1:
    print('You must provide the sub-directory.\nExample: python wallpape.py ~/Pictures/digitalcamera/rivers')
    sys.exit()

path = sys.argv[1]

goodBackgrounds = []
finishedDir = join(path, '1920w')
finishedDir2 = join(finishedDir, '16x9')

if not isdir(finishedDir):
    mkdir(finishedDir)

if not isdir(finishedDir2):
    mkdir(finishedDir2)

counter = 0
for file in listdir(path):
    if file.endswith('.jpg') or file.endswith('.png'):
        filePath = join(path, file)
        openImage = Image.open(filePath)
        if openImage.size[0] > openImage.size[1] and openImage.size[0] >= 1920:
            counter += 1
            move(filePath, finishedDir)
        openImage.close()
print('%s image(s) at least 1920 pixels in width were found in %s and moved to %s.' % (counter, '/' + sys.argv[1], '/' + sys.argv[1] + '/1920w'))

counter = 0
for file in listdir(finishedDir):
    if file.endswith('.jpg') or file.endswith('.png'):
        filePath = join(finishedDir, file)
        openImage = Image.open(filePath)
        if openImage.size[0] / openImage.size[1] == 1920 / 1080:
            counter += 1
            move(filePath, finishedDir2)
        openImage.close()
print('%s image(s) meeting the 16:9 aspect ratio were found in %s and moved to %s.' % (counter, '/1920w', '/1920w/16x9'))

counter = 0
for file in listdir(finishedDir2):
    if file.endswith('.jpg') or file.endswith('.png'):
        filePath = join(finishedDir2, file)
        openImage = Image.open(filePath)
        if openImage.size[0] > 1920:
            counter += 1
            openImageCopy = openImage.resize((1920, 1080))
            openImageCopy.save(filePath)
            openImageCopy.close()
        openImage.close()
