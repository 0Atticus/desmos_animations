import time
import subprocess
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import cv2

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.set_window_size(1024, 600)
driver.maximize_window()


frames = sorted([img for img in os.listdir("input/") if img.endswith(".png")])


for count, frame in enumerate(frames):
    print(frame)
    command = subprocess.Popen(["python3", "desmos.py", "input/" + frame])
    time.sleep(5)
    driver.get("http://localhost:5000")
    time.sleep(3)
    driver.save_screenshot(f"{count}.png")
    os.system(f"mv {count}.png output/ && rm input/{frame.split('.')[0]}.pnm")
    os.system(f"pkill -f desmos.py")


images = sorted([img for img in os.listdir("output") if img.endswith(".png")])

frame = cv2.imread(os.path.join("output", images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter("output_video.avi", 0, 30, (width, height))

for i in range (len(os.listdir("output"))):
    video.write(cv2.imread(os.path.join("output", f"{i}.png")))   



cv2.destroyAllWindows()
video.release()