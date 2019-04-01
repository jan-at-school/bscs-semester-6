
'''
Requirments:
  pip install pillow
  pip install matplotlib
  pip install numpy
Run:
> python task1.py path/to/image path/to/outdir/ order centerweight
'''

import PIL
from PIL import Image
import numpy as np
import itertools
import sys
import os
import convolution
# open image
# you have to pass the input image path as input arg
image = Image.open(sys.argv[1])
image = image.convert("RGB")  # convert to signle channeled image


width, height = image.size
totalPixels = width * height

a = [[1, 1, 2, 2, 2, 1, 1],
     [1, 2, 2, 4, 2, 2, 1],
     [2, 2, 4, 8, 4, 2, 2],
     [2, 4, 8, 16, 8, 4, 2],
     [2, 2, 4, 8, 4, 2, 2],
     [1, 2, 2, 4, 2, 2, 1],
     [1, 2, 2, 4, 2, 2, 1],
     [1, 1, 2, 2, 2, 1, 1]]


print(a)
smoothingMask = np.array(a,np.float)
print(smoothingMask)
for i, j in itertools.product(range(smoothingMask.shape[0]), range(smoothingMask.shape[1])):
  smoothingMask[i,j] /= smoothingMask.shape[0] *smoothingMask.shape[1]



pixels = image.load()
convolution.convolve(pixels, image.size, smoothingMask, False)


outDir = sys.argv[2] + \
    '/gaussian/{inputFile}/'.format(inputFile=os.path.basename(sys.argv[1]))
if not os.path.exists(outDir):
    os.makedirs(outDir)
image.save(outDir+'_gaussian.jpg')
