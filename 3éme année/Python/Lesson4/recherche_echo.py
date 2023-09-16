from numpy import *

T = array([int()] * 20)

def saisir():
    n = int(input("donner n: "))
    while (n < 3) or (n > 20):
        n = int(input("donner n: "))
    return n

def remplir(T, n):
    T[0] = int(input("donner un nombre: "))
    for i in range(1, n):
        T[i] = int(input("donner un nombre: "))
        while T[i] <= T[i - 1]:
            T[i] = int(input("donner un nombe superieur: "))

def recherche_echo(T, n, x):
    d = 0
    f = n - 1
    m = (d + f) // 2
    while T[m] != x and d <= f:
        m = (d + f) // 2
        if T[m] < x:
            d = m + 1
        else:
            f = m - 1
    return T[m] == x

n = saisir()
remplir(T, n)
nombre_a_rechercher = 10
if recherche_echo(T, n, nombre_a_rechercher):
    print("existe")
else:
    print("n'existe pas")