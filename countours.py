import cv2
import numpy as np

def get_contours(filename):
    im = cv2.imread(filename)
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 90, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.ones(im.shape[:2], dtype="uint8") * 255
    cv2.drawContours(mask, contours, -1, 0, -1)
    img = cv2.bitwise_and(im, im, mask=mask)
    cv2.imwrite(f"{filename.split('.')[0]}.pnm", mask)
    cv2.imwrite(f"{filename.split('.')[0]}_mask.png", mask)

get_contours("kirbo.png")