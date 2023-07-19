from MF import *

Traffic = Distance = Price = 0
TisVB = TisB = TisN = TisS = DistisL = DistisA = DistisSh = PisVH = PisH = PisF = PisLow = 0
MarkArray = {x: 0 for x in range(20, 51)}

def Fuzzification():
    global Traffic, Distance
    global TisVB, TisB, TisN, TisS, DistisL, DistisA, DistisSh

    TisVB = mfTisVB(Traffic)
    TisB = mfTisB(Traffic)
    TisN = mfTisN(Traffic)
    TisS = mfTisS(Traffic)
    DistisL = mfDistisL(Distance)
    DistisA = mfDistisA(Distance)
    DistisSh = mfDistisSh(Distance)

def FuzzyInference():
    global TisVB, TisB, TisN, TisS, DistisL, DistisA, DistisSh, PisVH, PisH, PisF, PisLow

    PisVH = min(TisVB, DistisL)
    PisH = max(min(TisVB, DistisA), min(TisB, DistisL))
    PisF = max(min(TisVB, DistisSh), min(TisB, DistisA), min(TisN, DistisL))
    PisLow = max(TisS, min(DistisSh, 1 - TisVB))

def Composition():
    global PisVH, PisH, PisF, PisLow
    global PriceArray

    for i in range(50, 1001):
        PriceArray[i] = max(min(mfPisVH(i / 10), PisVH),
                            min(mfPisH(i / 10), PisH),
                            min(mfPisF(i / 10), PisF),
                            min(mfPisLow(i / 10), PisLow))

    def Defuzzyfication():
        global Price
        global PriceArray

        X = list(PriceArray.keys())
        Y = list(PriceArray.values())
        Price = LastMax(X,Y) / 10

    def Run():
        Fuzzification()
        FuzzyInference()
        Composition()
        Defuzzyfication()

    def Init():
        global Traffic, Distance
        Traffic = float(input('Traffic = '))
        Distance = float(input('Distance = '))

    def Terminate():
        global Price
        print('Price = ', Price)

    def Main():
        Init()
        Run()
        Terminate()

    if __name__=='__main__':
        Main()
