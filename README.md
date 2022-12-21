# Desmos Animations

>A respoitory for converting images into bezier curve latexes for the Desmos graphing calculator

>This project is a work in progress, I am working on animations and colors in the calculator

[windows usage](#windows-guide)

## Usage
---
> clone this repository and cd into it
```bash
git clone https://github.com/0Atticus/desmos_animations
cd desmos_animations/
```

>install dependancies
```bash
pip install -r requirements.txt
```

>render an image in desmos
```bash
python3 desmos.py [path/to/image]
```
>if prompted with a "page not responding" message, click the wait option, the image will load.

<br>

## Windows Guide 
---
>I built and rested this on linux, but it should work for windows.

<br>

>download this repository as ZIP and extract it into a folder
<img src="https://i.ibb.co/PMnJPRX/save.png" />

>make sure you have [python](https://www.python.org/) installed

>open your command prompt by presisng the windows key and typing "cmd"

>navigate to the folder containing the repository with
```bash
cd desmos_animations
```
>install requirements
```bash
pip install -r requirements.txt
```

>if pip is not installed:
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

>choose an image (simple ones work better) and [convert](https://cloudconvert.com/) it to a png if needed, then render it in desmos with:
```bash
python3 desmos.py [path/to/image]
```

> follow the link that pops up in the console (it should look like this: 127.0.0.1:5000)
