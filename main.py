try:
    fileobject = open("kereset.txt","r")
    tartalom = fileobject.readline()
    print(tartalom)
    fileobject.close()
except FileNotFoundError:
    print("XDDD")

from enum import Enum


class napok(Enum):
    Hetfo = 1
    Kedd = 2
    Szerda = 3
    Csutortok = 4
    Pentek = 5
    Szombat = 6
    Vasarnap = 7
