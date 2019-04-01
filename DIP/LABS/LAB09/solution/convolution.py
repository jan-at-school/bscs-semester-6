
'''
Requirments:
  pip install pillow
  pip install matplotlib
  pip install numpy
Run:
> python task1.py path/to/image path/to/outdir/ order
'''

import PIL
from PIL import Image
import numpy as np
import itertools
import sys
import os


def inBound(pixelOnImage, size):
    x, y = pixelOnImage
    if(x < 0 or y < 0 or x >= size[0] or y >= size[1]):
        return False
    else:
        return True


def convolve(pixels, size, mask, add=False):
    print(mask)
    width, height = size

    for x, y in itertools.product(range(width), range(height)):

        mWidth, mHeight = mask.shape
        convoluted = (0, 0, 0)
        for i, j in itertools.product(range(mWidth), range(mHeight)):
            pixelOnImage = ((x - (int(mWidth/2) - i)),
                            (y - (int(mHeight/2) - j)))
            # print(pixelOnImage)
            if(inBound(pixelOnImage, (width, height))):
                convoluted = (int(convoluted[0] + (mask[i, j] * pixels[pixelOnImage][0])),
                                int(convoluted[1] + (mask[i, j] * pixels[pixelOnImage][1])),
                                int(convoluted[2] + (mask[i, j] * pixels[pixelOnImage][2])))
            else:
                continue

        pixels[x, y] = (convoluted)
        print(x, width,convoluted)
