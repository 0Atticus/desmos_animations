# seperate image like before then use pillow floodfill to alternate fill colors for each section

import numpy as np
from PIL import Image, ImageDraw
from os import sys
from math import sqrt

base_img = Image.open(sys.argv[1])
width = base_img.size[0]
height = base_img.size[1]


init_image = np.zeros([height, width, 3], dtype=np.uint8)
init_image.fill(255)

for x in range(width):
    for y in range(height):
        color = base_img.getpixel((x, y))
        r1, g1, b1 = color

        surrounding_pixels = [(b, i) for b in range(x - 1, x + 2) for i in range(y - 1, y + 2) if i >= 0 and b >= 0 and i < height and b < width]

        new_color = (255, 255, 255)

        for pix in surrounding_pixels:
            comparing_color = base_img.getpixel(pix)

            if comparing_color != (0, 0, 0):
                r2, g2, b2 = comparing_color
                d = sqrt(0.3*(r1-r2)**2 + 0.59*(g1-g2)**2 + 0.11*(b1-b2)**2)

                if d > 55:
                    new_color = (0, 0, 0)
        
        init_image[y, x] = new_color

data = Image.fromarray(init_image)
data.save("piss.png")



