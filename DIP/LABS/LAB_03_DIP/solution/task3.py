

'''
python task3.py path/to/input 
'''



import PIL
from PIL import Image
import itertools
import numpy
import sys
from PIL import ImageDraw
import matplotlib.pyplot as plt 
image = Image.open(sys.argv[1])
image = image.convert("L") # convert to singal channeled image
image = image.point(lambda x: 0 if x<150 else 255, '1') # binarized image

width, height = image.size


sums = [0] * height
print(len(sums))

pixels = image.load()
for x in range(height):

	for y in range(width):
		if pixels[y,x] == 0:
			sums[x]= sums[x] + 1 # increment the row's total 


print(sums)
for x in range(1,height):
	# use two conditions: check if the row is suitably white. sometimes the diff can be greater than the threshold even there is text present in the row
	if sums[x]==0 or  (sums[x] < 80 and (sums[x] -sums[x-1] > 15 or sums[x-1] -sums[x] > 15)):
		# draw line
		for y in range(width): 
			pixels[y,x] = 0




image.show()