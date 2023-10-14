from numpy import *

T = array([int()] * 20)
R = array([int()] * 20)

def remplir(T, n):
    T[0] = int(input("donner un nombre: "))
    for i in range(1, n):
        T[i] = int(input("donner un nombre: "))
        while recherche_sep(T, i, T[i]):
            T[i] = int(input("donner un nombre different: "))

def affichage(T, n):
    for i in range(n):
        print(T[i])

def Tri(T, R, n):
    for i in range(n):
        nb = nbinf(T, n, T[i])
        R[nb - 1] = T[i]

def recherche_sep(T, n, x):
    i = 0
    while T[i] != x and i != n - 1:
        i += 1
    return T[i] == x

def nbinf(T, n , x):
    c = 0
    for i in range(n):
        if T[i] <= x:
            c += 1
    return c

n = int(input("donner taille: "))
remplir(T, n)
print("avant Tri")
affichage(T, n)
Tri(T, R, n)
print("Aprés Tri")
affichage(R, n)