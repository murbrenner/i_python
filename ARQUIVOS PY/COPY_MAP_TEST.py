import os
import shutil
import subprocess
import time
import pyautogui
import pandas as pd
import pygetwindow as gw
import keyboard

filename = 'D:\\ELABORATION.csv'
df = pd.read_csv(filename)

for i in df.index:
    filename2 = "D:\\{}\\FIND.csv".format(str(df['OS'][i]))
    df2 = pd.read_csv(filename2)
    findlocal = (str(df2['LOCALIDADE'][0]))
    findsetor = (str(df2['SETOR'][0]))
    findrota = (str(df2['ROTA'][0]))

    if findlocal == '111':
        loc2 = 'CENTRO'
    elif findlocal == '122':
        loc2 = 'VINHAIS'
    elif findlocal == '133':
        loc2 = 'COHAB'
    elif findlocal == '145':
        loc2 = 'CIDADE OPERÁRIA'
    elif findlocal == '151':
        loc2 = 'ANJO DA GUARDA'
    elif findlocal == '183':
        print('GRUPO ALSAN 183 NAO TEM MAPA')
        pass
    else:
        print('ERRO')

    print(findlocal, findsetor, findrota, sep=',', end=',')

    pastamap = "D:\\{}\\".format(str(df['OS'][i]))

    try:
        file3 = "D:\\MAPAS_CAPITAL\\LOC - {} - {}\\SETOR {}\\ROTAS\\ROTA {}.dwg".format(findlocal, loc2, findsetor,
                                                                                        findrota)
        shutil.copy(file3, pastamap)

    except:
        try:
            file3 = "D:\\MAPAS_CAPITAL\\LOC - {} - {}\\SETOR {}\\ROTAS\\ROTA 0{}.dwg".format(findlocal, loc2,
                                                                                         findsetor,
                                                                                         findrota)
            shutil.copy(file3, pastamap)

        except:
            try:
                file3 = "D:\\MAPAS_CAPITAL\\LOC - {} - {}\\SETOR {}\\ROTAS\\ROTA00{}.dwg".format(findlocal, loc2,
                                                                                         findsetor,
                                                                                         findrota)
                shutil.copy(file3, pastamap)

            except:
                try:
                    file3 = "D:\\MAPAS_CAPITAL\\LOC - {} - {}\\SETOR {}\\ROTAS\\ROTA0{}.dwg".format(findlocal, loc2,
                                                                                                     findsetor,
                                                                                                     findrota)
                    shutil.copy(file3, pastamap)

                except:
                    print('NAO TEM MAPA')
                    pass





    print(file3)

