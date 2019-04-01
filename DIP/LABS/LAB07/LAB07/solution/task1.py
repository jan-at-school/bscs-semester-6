
'''
Requirments: 
  pip install pillow
  pip install matplotlib
  pip install numpy
Run:
> python main.py path/to/image
'''

import PIL
from PIL import Image
import numpy as np
import itertools
import sys
import matplotlib.pyplot as plt
# open image
image = Image.open(sys.argv[1]) # you have to pass the input image path as input arg
image = image.convert("L")  # convert to signle channeled image



width, height = image.size
totalPixels = width* height

freq = [0] * 256  # fill
cProbability = [0] * 256  # fill zeros



# save original image histogram
freq = image.histogram()
a = np.array(image)
plt.hist(a.ravel(),  bins=256)
plt.ylabel('Probability')
plt.xlabel('Gray Level')
plt.savefig('inputhist.svg')




# HISTOGRAM EQUALIZATION 
prevSum = 0
for i in range(256):
    prevSum += freq[i]*1.0/totalPixels # add the probablity to calculate 
    cProbability[i] = prevSum

print(cProbability[255]) 

pixels = image.load()
for x, y in itertools.product(range(width), range(height)):
    pixels[x,y] = int((255 * cProbability[pixels[x,y]])) # (L-1) * cummulative probability


# save resulatant image and histogram
image.save('output.jpg')
a = np.array(image)
plt.hist(a.ravel(),  bins=256)
plt.savefig('outputhist.svg')