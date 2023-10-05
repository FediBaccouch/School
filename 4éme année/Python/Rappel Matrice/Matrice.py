from numpy import array
from random import randint

M = array([[int()] * 20] * 20)

def saisir(bi, bs):
    n = int(input("Donner n: "))
    while n < bi or n > bs:
        n = int(input("Donner n: "))
    return n

def remplir(M, n):
    for i in range(n):
        for j in range(n):
            M[i, j] = randint(2, 100)

def afficher(M, n):
    S = 0

    print("=====PRINT 1=====")
    for i in range(n):
        for j in range(n):
            S = S + M[i, j]
            print(M[i, j], end="\t")
        print()
    
    print("=====PRINT 2=====")
    for i in range(n):
        for j in range(n):
            print(M[j, i], end="\t")
        print()
    
    print("=====SOMME=====")
    print(S)

n = saisir(3, 20)
remplir(M, n)
afficher(M, n)