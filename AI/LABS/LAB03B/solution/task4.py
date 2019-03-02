from PIL import Image
import itertools
from PIL import ImageDraw
image = Image.open("res/input.png")

binarizedImage = image.convert("L")  # convert to singal channeled image
binarizedImage = binarizedImage.point(
    lambda x: 0 if x < 150 else 255, '1')  # binarized image
width, height = image.size


cx = 0
cy = 0
n = 0
for x, y in itertools.product(range(width), range(height)):
    if binarizedImage.getpixel((x, y)) == 0:
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
for x, y in itertools.product(range(width), range(height)):

    color = binarizedImage.getpixel((x, y))

    if color == 0:
        if x > right:
            right = x
        if x < left:
            left = x
        if y > bottom:
            bottom = y
        if y < top:
            top = y


print cx, cy


draw = ImageDraw.Draw(image)
draw.rectangle(((left, top), (cx, cy)), outline="red")
draw.rectangle(((cx, top), (right, cy)), outline="green")
draw.rectangle(((left, cy), (cx, bottom)), outline="blue")
draw.rectangle(((cx, cy), (right, bottom)), outline="yellow")

boxes = [((left, top), (cx, cy)),
         ((cx, top), (right, cy)),
         ((left, cy), (cx, bottom)),
         ((cx, cy), (right, bottom))]
print(boxes)
T = [0, 0, 0, 0]
i = -1
for box in boxes:

    bwidth = box[1][1] - box[0][1]
    bheight = box[1][0] - box[0][0]

    startx, starty = box[0]
    print(bwidth, bheight)
    i = i+1
    prev = binarizedImage.getpixel((0, 0))
    n = 0
    for x, y in itertools.product(range(bwidth), range(bheight)):
        curr = binarizedImage.getpixel((startx + x, starty + y))
        if curr == 255 and prev == 0:
            n = n + 1
        prev = curr
    T[i] = n


print(T)


image.show()
