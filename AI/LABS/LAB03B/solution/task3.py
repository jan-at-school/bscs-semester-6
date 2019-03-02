from PIL import Image
import itertools
from PIL import ImageDraw
image = Image.open("res/input.png")
image.convert("RGB")
width, height = image.size

cx = 0
cy = 0
n = 0
for x,y in itertools.product(range(width), range(height)):
	if image.getpixel((x, y)) == (0,0,0):
		cx = cx + x
		cy = cy + y
		n = n + 1
cx = cx / n
cy = cy / n


width, height = image.size
left = width
right = 0
top = height
bottom = 0
for x,y in itertools.product(range(width), range(height)):
	
	color = image.getpixel((x,y))

	if color == (0,0,0):
		if x > right:
			right = x
		if x < left:
			left = x
		if y > bottom:
			bottom = y
		if y < top:
			top = y



'''
1.	(left, cx, top, cy) are the boundaries of top-left segment
2.	(cx, right, top, cy) are the boundaries of top-right segment
3.	(left, cx, cy, bottom) are the boundaries of bottom-left segment
4.	(cx, right, cy, bottom) are the boundaries of bottom-right segment

'''

print('Center: ', cx,cy)


draw = ImageDraw.Draw(image)
draw.rectangle(((left,top), (cx,cy)) ,outline = "red")
draw.rectangle(((cx, cy), (right, bottom)) ,outline = "yellow")
draw.rectangle(((left, cy), (cx, bottom)) ,outline = "blue")
draw.rectangle(((cx, top), (right, cy)) ,outline = "green")
image.show()
image.save('output/task3.png')
