from pynput.keyboard import Key, Controller
keyboard = Controller()

def input(latex):
    for bezier in latex:
        keyboard.type(str(bezier))
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

input(["pepie", "again"])