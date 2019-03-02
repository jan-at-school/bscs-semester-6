from PIL import Image
import itertools
from PIL import ImageDraw
image = Image.open("res/input.png")
image.convert("RGB")
width, height = image.size
left = width
right = 0
top = height
bottom = 0
for x,y in itertools.product(range(width), range(height)):
	
	color = image.getpixel((x,y))

	if color == (0,0,0):
		print x,y
		if x > right:
			right = x
		if x < left:
			left = x
		if y > bottom:
			bottom = y
		if y < top:
			top = y



print left ,top ,right,  bottom


draw = ImageDraw.Draw(image)
draw.rectangle(((left,top), (right,bottom)) ,outline = "black")
image.show()
image.save('output/task1.png')



