import numpy as np
from PIL import Image
from os import sys
import math

base_img = Image.open(sys.argv[1])
width = base_img.size[0]
height = base_img.size[1]


init_image = np.zeros((height, width, 3), dtype=np.uint8)
init_image.fill(255)

new_color = (255, 255, 255)

for y in range(height):
    new_color = (255, 255, 255)
    for x in range(width):
        color = base_img.getpixel((x, y))
        r1, g1, b1 = color
        if(x > 0):
            prev_pix = base_img.getpixel((x-1, y))
            

            r2, g2, b2 = prev_pix
            d = round(math.sqrt(0.3*(r1-r2)**2 + 0.59*(g1-g2)**2 + 0.11*(b1-b2)**2))
            
            if d > 55:
                if new_color == (255, 255, 255):
                    new_color = (0, 0, 0)
                else:
                    new_color = (255, 255, 255)

        init_image[y, x] = new_color

data = Image.fromarray(init_image)
data.save("piss.png")