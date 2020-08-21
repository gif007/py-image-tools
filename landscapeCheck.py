#!/bin/python
from PIL import Image
import os, sys, shutil

if len(sys.argv) < 2:
    print('Example Usage: landscapeCheck ~/Pictures/image-set/')
    print('Please include a path to a directory containing images.')
    sys.exit()

if not os.path.isdir(sys.argv[1]):
    print('That is not a valid directory.')
    sys.exit()
    
# variables

extensions = ['.jpg', '.png']
images = []
landscapes = []
name = input('Choose a name prefix for copied files: ')
path = sys.argv[1]

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
for x, y in enumerate(landscapes): # check if enumerate can begin at 1
    x += 1
    if y.endswith('.jpg'):
        dest = '/home/bard/dropbox/work/' + name + str(x) + '.jpg'
    else:
        dest = '/home/bard/dropbox/work/' + name + str(x) + '.png'
    shutil.copy(y, dest)

print('Completed.')
