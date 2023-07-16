import os
import shutil
import subprocess
import time
import pyautogui
import pandas as pd
import pygetwindow as gw
import keyboard
from keyboard import press


filename = 'D:\\ELABORATION.csv'
df = pd.read_csv(filename)


    # filename2 = "D:\\{}\\FIND.csv".format(str(df['OS'][i]))
    # df2 = pd.read_csv(filename2)
    # findlocal = (str(df2['LOCALIDADE'][0]))
    # findsetor = (str(df2['SETOR'][0]))
    # findrota = (str(df2['ROTA'][0]))

    # if findlocal == '111':
    #     loc2 = 'CENTRO'
    # elif findlocal == '122':
    #     loc2 = 'VINHAIS'
    # elif findlocal == '133':
    #     loc2 = 'COHAB'
    # elif findlocal == '145':
    #     loc2 = 'CIDADE OPERÁRIA'
    # elif findlocal == '151':
    #     loc2 = 'ANJO DA GUARDA'
    # elif findlocal == '183':
    #     print('GRUPO ALSAN 183 NAO TEM MAPA')
    #     pass
    # else:
    #     print('ERRO')

    #pastamap = "D:\\{}\\".format(str(df['OS'][i]))

file_path = "D:\\MAPAS_CAPITAL\\LOC - 122 - VINHAIS\\SETOR 109\\ROTAS\\ROTA 04.dwg"
subprocess.run([file_path], shell=True)

time.sleep(3)

pyautogui.press('enter')









#pyautogui.keyUp('enter')

# pyautogui.keyUp('shift')
# pyautogui.keyUp('A')
# pyautogui.hotkey('ctrl', 'p')




