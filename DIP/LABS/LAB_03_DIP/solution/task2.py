

'''
python task2.py path/to/input
'''



import PIL
from PIL import Image
import itertools
import numpy
import sys
from PIL import ImageDraw
import matplotlib.pyplot as plt
image = Image.open(sys.argv[1])
image = image.convert("L")  # convert to signle channeled image


width, height = image.size


intensities = [0] * 256  # fill zeros

pixels = image.load()  # allows pixel values to be edited
for x, y in itertools.product(range(width), range(height)):
    # print pixels[x,y]
    intensities[pixels[x, y]] = intensities[pixels[x, y]] + 1 # increment the same index as the value of the pixel


range = (0, 255)
bins = 256
print(intensities)
plt.hist(intensities, bins, range, color='green',
         histtype='bar', rwidth=0.8)


plt.show()
