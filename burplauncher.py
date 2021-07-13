import subprocess
import threading
from pynput.keyboard import Key,Controller
import time

import os


def th():
    keyboard = Controller()
    time.sleep(1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def kill():
    time.sleep(2)
    subprocess.call("taskkill/IM javaw.exe",shell=True)

t = threading.Thread(target=th)
s = threading.Thread(target=kill)


t.start()
s.start()
os.chdir("G:\\Application\\burp")
subprocess.call("burploader.jar",shell=True)