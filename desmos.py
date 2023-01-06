import cv2
import numpy as np
from PIL import Image
import potrace
import time
from flask import Flask, render_template
from os import sys, system
import math


app = Flask(__name__)



def get_latex(filename):
    latex = []
    img = Image.open(filename)
    data = np.asarray(img)
    bmp = potrace.Bitmap(data)
    path = bmp.trace()

    for curve in path.curves:
        segments = curve.segments
        start = curve.start_point
        for segment in segments:
            x0, y0 = start.x, start.y
            if segment.is_corner:
                x1, y1 = segment.c.x, segment.c.y
                x2, y2 = segment.end_point.x, segment.end_point.y
                latex.append('((1-t)%f+t%f,(1-t)%f+t%f)!' % (x0, x1, y0, y1))
                latex.append('((1-t)%f+t%f,(1-t)%f+t%f)!' % (x1, x2, y1, y2))
            else:
                x1, y1 = segment.c1.x, segment.c1.y
                x2, y2 = segment.c2.x, segment.c2.y
                x3, y3 = segment.end_point.x, segment.end_point.y
                latex.append('((1-t)((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f))+t((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f)),\
                (1-t)((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f))+t((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f)))!' % \
                (x0, x1, x1, x2, x1, x2, x2, x3, y0, y1, y1, y2, y1, y2, y2, y3))
            start = segment.end_point
    return latex


def get_contours(filename):
        
    im = cv2.imread(filename)
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 110, 190, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.ones(im.shape[:2], dtype="uint8") * 255
    cv2.drawContours(mask, contours, -1, 0, -1)
    img = cv2.bitwise_and(im, im, mask=mask)
    cv2.imwrite(f"{filename.split('.')[0]}.pnm", mask)
    return (f"{im.shape[1]},{im.shape[0]}")
    
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

def get_points(filename):
    colors = []
    points = ""
    img = Image.open(filename)
    for y in range(img.height):
        for x in range(img.width):
            if (x % 10 == 0 and x > 0):
                if (y % 10 == 0):
                    points += f"(-{x}, -{y})~"
                    colors.append(rgb_to_hex(img.getpixel((x, y))))
    return (points[:-1], colors)

def flip_image(filename):
    img = Image.open(filename)
    hzimg = img.transpose(method=Image.FLIP_LEFT_RIGHT)
    hzimg.save(filename)


def seperate_colors(filename):
    base_img = Image.open(filename)
    width = base_img.size[0]
    height = base_img.size[1]

    init_image = np.zeros((height, width, 3), dtype=np.uint8)
    init_image.fill(255)

    new_color = (255, 255, 255)

    for y in range(height):
        new_color = (255, 255, 255)
        for x in range(width):
            color = base_img.getpixel((x, y))
            r1, g1, b1 = color[0], color[1], color[2]
            if(x > 0):
                prev_pix = base_img.getpixel((x-1, y))
                

                r2, g2, b2 = prev_pix[0], prev_pix[1], prev_pix[2]
                d = round(math.sqrt(0.3*(r1-r2)**2 + 0.59*(g1-g2)**2 + 0.11*(b1-b2)**2))
                
                if d > 50:
                    if new_color == (255, 255, 255):
                        new_color = (0, 0, 0)
                    else:
                        new_color = (255, 255, 255)

            init_image[y, x] = new_color

    data = Image.fromarray(init_image)
    data.save("piss.png")


@app.route("/")
def plot_image():

    filename = sys.argv[1]
    colored = filename
    colors = ""
    points = ""

    if "--detail" in sys.argv:
        seperate_colors(filename)
        system(f"mv piss.png {filename.split('.')[0]}_bw.png")
        filename = f"{filename.split('.')[0]}_bw.png"
    
    flip_image(filename)
    shape = get_contours(filename)
    raw_latex = get_latex(filename.split(".")[0] + ".pnm")
    latex = ""
    flip_image(filename)

    if ("--color" in sys.argv):
        flip_image(colored)
        points, c = get_points(colored)
        flip_image(colored)

        
        for i in c:
            colors += str(i) + "~"
    
    latex = "".join(raw_latex)

    return render_template("index.html", colors=colors, points=points, latex=latex, shape=shape)


    
if __name__ == "__main__":
    app.run()

