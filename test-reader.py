from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

def on_click(x, y, button, pressed):
    if pressed:
        print(f'Mouse button pressed: {button}')
    else:
        print(f'Mouse button released: {button}')
        
def on_press(key):
    print(f'Key pressed: {key}')

def on_release(key):
    print(f'Key released: {key}')

with KeyboardListener(on_press=on_press, on_release=on_release) as kl, MouseListener(on_click=on_click) as ml:
    ml.join()
    kl.join()