
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

order = int(sys.argv[3])
a = [[1/(order*order)] * order]*order

centerWeight = int(sys.argv[4])
a = [[1/9, 1/9, 1/9],
     [1/9, centerWeight/9, 1/9],
     [1/9, 1/9, 1/9]]
print(a)
smoothingMask = np.array(a)

print(smoothingMask)


pixels = image.load()
convolution.convolve(pixels, image.size, smoothingMask, False)



outDir = sys.argv[2] + '/smoothing/{inputFile}/'.format(inputFile=os.path.basename(sys.argv[1]))
if not os.path.exists(outDir):
    os.makedirs(outDir)
image.save(outDir+'{order}x{order}_centerweight_{centerWeight}.jpg'.format(order=order,centerWeight=centerWeight))
