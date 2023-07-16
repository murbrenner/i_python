import subprocess
import time

import pyautogui

subprocess.run(['start', "D:\\4164115\\123.pdf"], shell=True)
time.sleep(1.5)
pyautogui.hotkey('ctrl', 'f')
time.sleep(1.5)
pyautogui.typewrite("111.102.609.0143.000")
time.sleep(0.5)
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')

pyautogui.hotkey('ctrl', 'p')
time.sleep(1)

pyautogui.keyDown('alt')
pyautogui.keyDown('e')
pyautogui.keyUp('alt')
pyautogui.keyUp('e')
pyautogui.keyDown('down')
pyautogui.keyUp('down')
time.sleep(0.5)
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')






