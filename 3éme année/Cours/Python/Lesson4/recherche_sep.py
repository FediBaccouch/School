from numpy import *
from random import *

T = array([int()] * 20)

def saisir():
    n = int(input("donner n: "))
    while (n < 3) or (n > 20):
        n = int(input("donner n: "))
    return n

def remplir(T, n):
    for i in range(n):
        T[i] = randint(2, 70)

def recherche_sep(T, n, x):
    i = 0
    while T[i] != x and i != n - 1:
        i += 1
    return T[i] == x

n = saisir()
remplir(T, n)
nombre_a_rechercher = 10
if recherche_sep(T, n, nombre_a_rechercher):
    print("existe")
else:
    print("n'existe pas")