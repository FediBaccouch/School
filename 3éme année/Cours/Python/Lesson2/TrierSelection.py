from numpy import *

T = array([int()] * 15)

def saisir():
    n = int(input("donner n: "))
    while (n < 6) or (n > 15):
        n = int(input("donner n: "))
    return n

def remplir(T, n):
    for i in range(n):
        T[i] = int(input(""))

def affichage(T, n):
    for i in range(n):
        print(T[i])

def triSelection(T, n):
    for i in range(n - 1):
        p = i
        for j in range(i + 1, n):
            if T[j] < T[p]:
                p = j
        if p != i:
            aux = T[i]
            T[i] = T[p]
            T[p] = aux

n = saisir()
remplir(T, n)
print("*avant Tri*")
affichage(T, n)
print("*aprés Tri*")
triSelection(T, n)
affichage(T, n)