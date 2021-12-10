from etelek import etelfajtak

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


fileobject = open("kereset.txt", "r")
fileobject3 = open("csakkereset.txt", "w")
szoveg = fileobject.read()
for kar in szoveg:
    if kar in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "\n"):
        fileobject3.write(kar)
    else:
        fileobject3.write("")
fileobject.close()
fileobject3.close()


osszeg = 0
fileobject3 = open("csakkereset.txt", "r")
for sor in fileobject3:
    szam = int(sor)
    osszeg += szam
print(osszeg, "Ft bevételt szerzett a mai napon az étterem")
fileobject3.close()


fileobject2 = open("csaketelfajtak.txt", "r")
szoveg = fileobject2.read()
adottetelszama = szoveg.lower().count(etelfajtak.Csirke.value)
print(etelfajtak.Csirke.value, "-t a mai napon", adottetelszama, "-szor rendeltek")
fileobject2.close()

