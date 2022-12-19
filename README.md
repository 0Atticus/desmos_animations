
#  Desmos Animations
> A repository for converting images into bezier curve equations and drawing them with the desmos API.

>This project is a work in progress, it is functional but not complete.

>[Windows usage guide](#windows)

## Installation
Make sure you have [python](https://www.python.org) installed.
Clone this repository and install the dependancies
```bash
git clone https://github.com/0Atticus/desmos_animations
cd desmos_animations
pip install -r requirements.txt
```
## Documentation
> This project can convert both images and videos into desmos graphs.
> To render a single image, just run:
 ```bash
 python3 desmos.py [path/to/image]
 ```
>If you recieve a message that says the page is not responding, click wait, the page will load.
---

>If you want to convert a video, you first need to create a directory named "input" in this repository
```bash
mkdir input/
```
>Then, move your video into the directory and split it into seperate frames, then remove the original video if necessary. Be sure to use PNG images.
```bash
mv [my_video] input/
cd input/
ffmpeg -i [my_video] %04d.png
rm [my_video]
```
>Next, create an output folder and run main.py.
```bash
mkdir output/
python3 main.py
```
>This part of the project is under development and is not optimized, a 45 second video will take around 3 hours to render.

>After rendering, your completed video will be in the home folder with the name "output_video.avi"


## Windows

>download this repository and extract it into a folder.
>top left: code > download ZIP

<p align="center"><img src="https://i.ibb.co/600jgh5/Screenshot-2022-11-21-2-08-21-PM.png" alt="Screenshot-2022-11-21-2-08-21-PM" border="0"></p>

>make sure you have [python](https://www.python.org) installed.

>Press the start key and type 'cmd' to open your command prompt.
>Navigate to this repository with 
```bash
cd desmos_animations
```
>Install dependancies with:
```bash
pip install -r requirements.txt
```
>If pip is not installed:
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

> Choose an image (simple ones work better) and [convert](https://cloudconvert.com/) it to png if needed.
> Move the image to your desmos_animations folder and reopen the command prompt.
```bash
cd desmos_animations
python3 desmos.py [my_image.png]
```
>follow the link provided in the terminal (it should look like this: 127.0.0.1:5000) and wait. If you get a message that the page isn't responing, hit the wait option. the image will load.
