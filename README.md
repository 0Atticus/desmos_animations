#  Desmos Animations
> A repository for converting images into curve equations and drawing them with the desmos API.

>This project is a work in progress, it is functional but not complete.

## Installation
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
