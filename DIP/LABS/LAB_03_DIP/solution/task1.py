
'''
python task1.py path/to/input threshold-int
'''


import PIL
from PIL import Image
import itertools
import sys
from PIL import ImageDraw
image = Image.open(sys.argv[1])
image = image.convert("L") # convert to signle channeled image

width, height = image.size



pixels = image.load() # allows pixel values to be edited
for x,y in itertools.product(range(width), range(height)): # all possible values of x and y
	if pixels[x,y] > int(sys.argv[2]):
		pixels[x,y] = 255
	else:
		pixels[x,y] = 0




image.show()