import time
import subprocess
import webbrowser
import os
import cv2
import mss
from PIL import Image
import pyautogui

sct = mss.mss()

frames = sorted([img for img in os.listdir("input/") if img.endswith(".png")])

for count , frame in enumerate(frames):
    print(frame)
    command = subprocess.Popen([
        "python3", "desmos.py", "input/" + frame
    ])
    time.sleep(1)
    webbrowser.open("http://localhost:5000")


    while 1:
        box = {"left": 14, "top": 184, "width": 1, "height": 1}
        img = sct.grab(box)
        mss.tools.to_png(img.rgb, img.size, output="temp.png")
        color = Image.open("temp.png").getpixel((0, 0))
        if (color == (45,112,179)):
            break
        elif color == (230, 107, 60):
            pyautogui.moveTo(400, 175)
            pyautogui.click()
            time.sleep(1)
            break
        
        box = {"left": 813, "top": 269, "height": 1, "width": 1}
        img = sct.grab(box)
        mss.tools.to_png(img.rgb, img.size, output="temp.png")
        color = Image.open("temp.png").getpixel((0, 0))
        if (color == (26, 115, 232)):
            pyautogui.moveTo(813, 269)
            pyautogui.click()
        
    img = sct.grab({"left": 0, "top": 110, "width": 1366, "height": 728-110})
    name = int(str(frame).split(".")[0])
    mss.tools.to_png(img.rgb, img.size, output=f"output/{name}.png")

    os.system("rm input/" + str(frame).split(".")[0] + ".*")
    
    os.system("pkill -f desmos.py")
    os.system("pkill chrome")

images = sorted([img for img in os.listdir("output") if img.endswith(".png")])

frame = cv2.imread(os.path.join("output", images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter("output_video.avi", 0, 30, (width, height))

for i in range(len(os.listdir("output"))):
    video.write(cv2.imread(os.path.join("output", f"{i}.png")))

cv2.destroyAllWindows()
video.release()
