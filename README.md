# SimplePythonMacros
A simple implementation of macros through pynput and pyautogui. Will continue to build out as interest waxes.

For now, usage is as simple as constructing a macros file macros.mac of the format:

```
<macro keys>:<action sequence>
```
**\<macro keys\>** can be any combination of keys and mouse buttons, combos separated by '+'.

**\<action sequence\>** is a list of actions, separated by '>'. Each action is a list of keys, mouse buttons, and combos.

Example: 

```
alt+w: w>space>k  # will type 'w<space>k'
alt+e: ctrl+8     # will press ctrl+8
```            
  
Then, after your macro file is built, run the general-macro-boy.py script.