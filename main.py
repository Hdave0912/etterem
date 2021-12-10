from etelek import etelek_beszerzes

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
print(osszeg, "Ft értékben rendeltek ma az étteremtől\n")
fileobject3.close()


def bevetel():
    """Az étterem a napi jövedelem 10%-át elutalja rászoruló családoknak, majd a maradék pénz 5%-át odaadják a hónap
    dolgozójának """
    bevetel = osszeg * 0.9
    bevetel = bevetel * 0.95
    print(bevetel, "Ft bevételt szerzett a mai napon az étterem\n")


bevetel()


def etelvalasztas():
    print("Adjon meg egy állatfajtát a lekérdezéshez:")
    valasz = None
    while valasz not in ("Csirke", "Marha", "Hal", "Szarvas", "Sertes"):
        valasz = input("Az alábbiak közül válasszon: (Csirke, Marha, Hal, Szarvas, Sertes)\n")
    return valasz


fileobject2 = open("csaketelfajtak.txt", "r")
szoveg = fileobject2.read()
adotteteldbszama = szoveg.count(etelvalasztas())
print(adotteteldbszama, "-szor/szer rendeltek az adott állat fajtából\n")
fileobject2.close()


print("Adjon meg egy állatot, hogy megtudja honnan szerezzük be!\n")
print( etelek_beszerzes[etelvalasztas()].value,
      "ről/ról/ből szerezzük be az állatot")
