#!/bin/python

from PIL import Image
from os import listdir, mkdir
from os.path import join, isdir
from shutil import move
from ArgumentParser import parser

args = parser.get_args()
path = args.path

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
if args.verbose: print('%s image(s) at least 1920 pixels in width were found in %s and moved to %s.' % (counter, path, join(path, '1920w')))

counter = 0
for file in listdir(finishedDir):
    if file.endswith('.jpg') or file.endswith('.png'):
        filePath = join(finishedDir, file)
        openImage = Image.open(filePath)
        if openImage.size[0] / openImage.size[1] == 1920 / 1080:
            counter += 1
            move(filePath, finishedDir2)
        openImage.close()
if args.verbose: print('%s image(s) meeting the 16:9 aspect ratio were found in %s and moved to %s.' % (counter, '1920w', join('1920w', '16x9')))

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
print('complete')