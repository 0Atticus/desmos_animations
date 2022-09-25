import os
import cv2

images = sorted([img for img in os.listdir("output") if img.endswith(".png")])

frame = cv2.imread(os.path.join("output", images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter("output_video.avi", 0, 30, (width, height))

for i in range (len(os.listdir("output"))):
    video.write(cv2.imread(os.path.join("output", f"{i}.png")))   



cv2.destroyAllWindows()
video.release()