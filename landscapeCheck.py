#!/bin/python
from PIL import Image
import os, sys, shutil

if len(sys.argv) == 2 and sys.argv[1] == '--help':
    print('Example Usage: landscapeCheck ~/Pictures/image-set/\nIf no path is included the utility will use the present working directory.')
    sys.exit()

if len(sys.argv) == 2:
    if not os.path.isdir(sys.argv[1]):
        print('That is not a valid directory.')
        sys.exit()
    else:
        path = sys.argv[1]

if len(sys.argv) == 1:
    path = os.getcwd()
    
# variables

extensions = ['.jpg', '.png']
images = []
landscapes = []
name = input('Choose a name prefix for copied files or leave blank if you wish to retain original filenames: ')

# functions

# populate a list with every file that is an image
for i in os.listdir(path):
    if i[-4:] in extensions:
        images.append(os.path.join(path, i))

# populate a new list with only images that are landscape orientation
for j in images:
    currentImage = Image.open(j)
    width, height = currentImage.size
    if width > height:
        landscapes.append(j)

# exit if no landscapes were found
if len(landscapes) == 0:
    print('No landscape images could be found.')
    sys.exit()
else:
    landscapes.sort()

# display all of the landscape results
print('The following images are landscape:')
for s in landscapes:
    print(os.path.basename(s))

# confirm if user wants to copy
while True:
    choice = input('Do you wish to copy these to your work folder? (y/N): ')
    if choice.lower() == 'y':
        break
    elif choice.lower() == 'n':
        sys.exit()
    else:
        print('Not a valid input.')
        sys.exit()

# copy the images with a new name
### improve this with regex ###
destPath = os.path.join(path, 'landscapes')
if not os.path.isdir(destPath):
    os.mkdir(destPath)

for x, y in enumerate(landscapes): # check if enumerate can begin at 1
    x += 1
    if name:
        if y.endswith('.jpg'):
            dest = os.path.join(destPath, name + str(x) + '.jpg')
        else:
            dest = os.path.join(destPath, name + str(x) + '.png')
    else:
        dest = os.path.join(destPath, os.path.basename(y))

    shutil.copy(y, dest)

print('Completed.')
