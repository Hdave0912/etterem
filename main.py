from enum import Enum
class etelfajtak(Enum):
    Csirke = 1

fileobject = open("kereset.txt", "r")
fileobject2 = open("csaketelfajtak.txt", "w")
szoveg = fileobject.read()
for kar in szoveg:
    if kar in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', " "):
        fileobject2.write("")
    else:
        fileobject2.write(kar)
fileobject.close()
fileobject2.close()

counter = 0
fileobject2 = open("csaketelfajtak.txt", "r")
data = fileobject2.read()
for sor in fileobject2:
    counter = sor.count('Csirke')
print(counter)
fileobject2.close()

