import cv2
import numpy as np
from PIL import Image
import potrace
import time
from flask import Flask, render_template
from os import sys, system

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
    


def flip_image(filename):
    img = Image.open(filename)
    hzimg = img.transpose(method=Image.FLIP_LEFT_RIGHT)
    hzimg.save(filename)


@app.route("/")
def plot_image():
    flip_image(filename)
    shape = get_contours(filename)
    raw_latex = get_latex(filename.split(".")[0] + ".pnm")
    latex = ""
    flip_image(filename)
    for bezier in raw_latex:
        latex += bezier
    return render_template("index.html", latex=latex, shape=shape)


if __name__ == "__main__":
    filename = sys.argv[1]
    app.run()
