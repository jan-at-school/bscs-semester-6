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




print cx,cy


draw = ImageDraw.Draw(image)
draw.rectangle(((cx,cy), (cx+5,cy+5)) ,outline = "red")
image.show()
image.save('output/task2.png')
