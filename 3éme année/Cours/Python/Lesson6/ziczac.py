from numpy import *

position = dict(NL = int(), NC = int())
Eng = dict(val = int(), pos = position)
Mat = array([[int] * 12] * 5)
T = array([Eng] * 100)

def saisir(N, a, b):  # N est juste pour afficher L ou C au lieu de N dans l'input
    n = int(input("donner " + N + ": "))
    while n < a or n > b:
        n = int(input("donner " + N + ": "))
    return n

def remplir(Mat, L, C):
    for i in range(L):
        for j in range(C):
            Mat[i, j] = int(input("Mat[" + str(i) + ", " + str(j) + "] = "))
            while len(str(Mat[i, j])) % 4 == 0:
                Mat[i, j] = int(input("Mat[" + str(i) + ", " + str(j) + "] = "))

def afficher(T, n):
    print("")  # pour que l'affichage fasse un espace entre les données d'utilisateur et les données d'affichage
    for i in range(n + 1):
        print(T[i]["val"])
        print(T[i]["pos"]["NL"])
        print(T[i]["pos"]["NC"])
        print("------------")  # pour que l'affichage fasse un espace entre les différentes données de tableau T

def construit(Mat, T, L, C):
    n = -1
    for i in range(L):
        for j in range(C):
            if ziczac(Mat[i, j]):
                n += 1
                T[n] = {}
                T[n]["val"] = Mat[i, j]
                T[n]["pos"] = {}
                T[n]["pos"]["NL"] = i
                T[n]["pos"]["NC"] = j
    return n

def ziczac(m):
    ch = str(m)
    ch1 = ch[:len(ch) // 2 + 1]
    ch2 = ch[len(ch) // 2:len(ch)]
    r1 = Tri_Croi(ch1)
    r2 = Tri_Dec(ch2)
    if ch1 == r1 and ch2 == r2:
        ok = True
    else:
        ok = False    
    return ok

def Tri_Croi(ch):
    permut = True
    while permut:
        permut = False
        for i in range(len(ch) - 1):
            if ch[i] > ch[i + 1]:
                ch = ch[:i] + ch[i + 1] + ch[i] + ch[i + 2:]
                permut = True
    return ch

def Tri_Dec(ch):
    permut = True
    while permut:
        permut = False
        for i in range(len(ch) - 1):
            if ch[i] < ch[i + 1]:
                ch = ch[:i] + ch[i + 1] + ch[i] + ch[i + 2:]
                permut = True
    return ch

L = saisir("L", 3, 5)
C = saisir("C", 6, 12)
remplir(Mat, L, C)
n = construit(Mat, T, L, C)
afficher(T, n)