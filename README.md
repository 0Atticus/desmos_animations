
# Desmos Animations

>A repository for converting images into bezier curve latices for the Desmos graphing calculator

>This project is a work in progress, I am working on animated graphs as well as a better image mask.



## Linux
> Clone this repository and cd into it.
```bash
git clone https://github.com/0Atticus/desmos_animations
cd desmos_animations/
```

>Install dependencies.
```bash
pip install -r requirements.txt
```

>Render an image in Desmos.
```bash
python3 desmos.py [path/to/image]
```
>The time to load depends on the number of lines in the image as well as the size, all images will load eventually.

> Add "--color" to your arguments to render the image in color.
<br>

## Windows 
>I built and tested this on Linux, but it should work for windows.

<br>

>Download this repository and extract it into a folder.
<img src="https://i.ibb.co/PMnJPRX/save.png" />

>Make sure you have [python](https://www.python.org/) installed.

>Open your command prompt by pressing the windows key and typing "cmd"

>Navigate to the folder containing the repository with:
```bash
cd desmos_animations
```
>Install requirements.
```bash
pip install -r requirements.txt
```

>If pip is not installed:
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

>Choose an image (simple ones work better), move it into your "desmos_animations" folder, and render it in Desmos with:
```bash
python3 desmos.py [your_image.png]
```

>Follow the link that pops up in the console. (it should look like this: 127.0.0.1:5000)

>If you want to render in color, use this command:
```bash
python3 desmos.py [your_image.png] --color
```

## Saving your Graph

> You might want to save the graph you made, to do that you need to transfer it to the actual Desmos website.
>To do this, Desmos has a function that can get the state of the calculator, but we have to put in a little work ourselves.

>First, open the graph you generated with this program and open the console (CTRL + SHIFT + J or right click > inspect > console) and type this command in, and hit enter.
```javascript
calculator.getState();
```
>Right below the command you should see a result, right click it and click the "Copy object" option.
<img src="https://i.ibb.co/vQ5M5MK/Screenshot-2023-01-04-1-54-12-PM.png" alt="Screenshot-2023-01-04-1-54-12-PM" border="0">

>Now, open [Desmos](https://www.desmos.com/calculator) and open the console again.
>This time, type this command but don't press enter yet.
```javascript
Calc.setState();
```
>move your cursor between the parentheses and paste the object you copied with CTRL + V, then hit enter and wait for the graph to load.
>After it has loaded, there will be a "save" button at the top of the screen you can use to save the graph to your account. (you will need to be logged in)


## How it Works (Summarized)

> First, we apply an [OpenCV](https://opencv.org/) mask to convert the image to black and white
> 
> After applying the mask, we use [Potrace](https://potrace.sourceforge.net/), which converts the black and white bitmap image to a vector image.
> 
> Using Potrace again, we read from the raster image and convert each line segment into a bezier curve.
> 
> If we are rendering with color, we create a point on the graph for every 100th pixel in the image. The point will be the same color as that pixel.
> 
> Using [Flask](https://flask.palletsprojects.com/) and the [Desmos API](https://www.desmos.com/api/v1.7/docs/index.html), we load all of our equations into a graph that is displayed for the user.
