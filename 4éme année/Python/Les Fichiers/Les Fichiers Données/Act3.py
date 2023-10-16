from pickle import load, dump

Eng = dict(nb=int(), P=bool())

def saisir(bi, bs):
    n = int(input("Donner n: "))
    while n < bi or n > bs:
        n = int(input("Donner n: "))
    return n

def remplir(F, n):
    for i in range(n):
        x = int(input("Donner x: "))
        while x <= 0:
            x = int(input("Donner x: "))
        dump(x, F)
    F.close()

def former(FP, F, n):
    F = open("./nombres.dat", "rb")

    for i in range(1, n + 1):
        x = load(F)
        Eng["nb"] = x
        Eng["P"] = premier(x)
        dump(Eng, FP)
    F.close()
    FP.close()

def premier(x):
    i = 2
    while x % i != 0 and i <= x // 2:
        i = i + 1
    return i > x // 2

def afficher(FP):
    FP = open("./premiers.dat", "rb")
    fin_ficher = False
    while not fin_ficher:
        try:
            Eng = load(FP)
            print(Eng["nb"], end="\t")
            print(Eng["P"])
        except:
            fin_ficher = True
    FP.close()

n = saisir(2, 100)
F = open("./nombres.dat", "wb")
FP = open("./premiers.dat", "wb")
remplir(F, n)
former(FP, F, n)
afficher(FP)