from BasicFunctions import *

def mfTisS(x):
    return SmZ(x, 3, 4.5)

def mfTisN(x):
    return SmTrap(x, 2.5, 3, 5.5, 8)

def mfTisB(x):
    return SmTrap(x, 5, 6.5, 9, 10)

def mfTisVB(x):
    return SmS(x, 8, 9)


def mfDistisSh(x):
    return SmZ(x, 20, 35)

def mfDistisA(x):
    return SmTrap(x, 15, 20, 85, 95)

def mfDistisL(x):
    return SmS(x, 70, 85)


def mfPisLow(x):
    return SmZ(x, 25, 45)

def mfPisF(x):
    return SmTrap(x, 15, 25, 60, 75)

def mfPisH(x):
    return SmTrap(x, 50, 60, 90, 100)

def mfPisVH(x):
    return SmS(x, 75, 90)


