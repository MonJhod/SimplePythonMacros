'''
File: general-macro-boy.py
Author: John Dominguez (MonJhod)
Date: 2023-12-31
Description: This code sets up keyboard and mouse listeners to execute macro actions when 
             certain keys are pressed or mouse buttons are clicked. It loads the macro 
             definitions from a macros.mac file, parses them, and stores them in a dict.
             The format for the macros.mac file is as follows:
                <macro keys>:<action sequence>
                
                <macro keys> can be any combination of keys and mouse buttons, combos separated by '+'.
                <action sequence> is a list of actions, separated by '>'. Each action is a list of keys,
                mouse buttons, and combos.
                
                Example: 
'''

import pyautogui
pyautogui.FAILSAFE = True

import random
from pynput import keyboard, mouse
import time

def parse_macro_line(line):
    trigger, action = line.strip().split(':')
    action_sequence = action.strip().split('>')
    return trigger.strip(), [key.strip().split('+') for key in action_sequence]

def execute_action_sequence(action_sequence):
    for action in action_sequence:
        pyautogui.hotkey(*action)
        time.sleep(random.uniform(0.05, 0.1))  # Short delay between key presses

def on_press(key):
    try:
        key_name = str(key).replace("'", "")
        if key_name in macros:
            execute_action_sequence(macros[key_name])
    except Exception as e:
        print(f"Error: {e}")

def on_click(x, y, button, pressed):
    button_name = str(button).split('.')[-1]
    if pressed and button_name in macros:
        execute_action_sequence(macros[button_name])

# Load macros from file
macros = {}
with open('macros.mac', 'r') as file:
    for line in file:
        trigger, action_sequence = parse_macro_line(line)
        macros[trigger] = action_sequence

# Setup listeners
keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_click)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()
