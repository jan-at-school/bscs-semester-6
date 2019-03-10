
from PIL import Image
import itertools
from PIL import ImageDraw
from methods import BOX
import numpy as np
import methods
import os

sig = 'R0001'
path = 'res'
mime = '.png'



image = Image.open(path+'/'+sig+mime)

binarizedImage = image.convert("L")  # convert to singal channeled image
binarizedImage = binarizedImage.point(
    lambda x: 0 if x < 150 else 255, '1')  # binarized image

width, height = image.size


draw = ImageDraw.Draw(image)

centroids = np.zeros((0, 2), np.int)
ratios = np.zeros((0, 1), np.int)
transitions = np.zeros((0, 1), np.int)


def findRatio(box):
    return (box.right-box.left)*1.00/(box.bottom-box.top)


def split(image, thisBox, depth=0):
    cx, cy = methods.centroid(binarizedImage, thisBox)
    print(cx, cy)
    if depth < 3:
        split(image, BOX(thisBox.left, cx, thisBox.top, cy), depth + 1)
        split(image, BOX(cx, thisBox.right, thisBox.top, cy), depth + 1)
        split(image, BOX(thisBox.left,
                         cx, cy, thisBox.bottom), depth + 1)
        split(image, BOX(cx, thisBox.right, cy, thisBox.bottom), depth + 1)

    else:
        t = methods.transitions(image, thisBox)
        r = findRatio(thisBox)
        
        centroids = np.append(centroids, [[cx, cy]])
        transitions = np.append(transitions, [t])
        ratios = np.append(ratios, [r])
        # transitions[currentBox] = t
        # ratios[currentBox] = r
        # currentBox += 1
        print(t, r)

        draw.rectangle(((thisBox.left, thisBox.top),
                        (thisBox.right, thisBox.bottom)), outline="yellow")


mainBox = methods.boundaries(binarizedImage)
print(mainBox)
split(binarizedImage, mainBox)


if not os.path.exists('processed/centroids'):
    os.makedirs('processed/centroids')

if not os.path.exists('processed/transitions'):
    os.makedirs('processed/transitions')

if not os.path.exists('processed/ratios'):
    os.makedirs('processed/ratios')


np.savetxt('processed/centroids/'+sig+'.txt', centroids)
np.savetxt('processed/transitions/'+sig+'.txt', transitions)
np.savetxt('processed/ratios/'+sig+'.txt', ratios)

image.show()
