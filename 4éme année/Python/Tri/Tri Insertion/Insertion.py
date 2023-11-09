from numpy import array

T = array([int()] * 20)

def saisir(bi, bs):
    n = int(input("Donner N: "))
    while n < bi or n > bs:
        n = int(input("Donner N: "))
    return n

def remplir(T, n):
    for i in range(n):
        T[i] = int(input("T[" + str(i) + "] = "))

def tri(T, n):
    for i in range(1, n):
        v = T[i]
        p = i
        while T[p - 1] > v and p >= 0:
            T[p] = T[p - 1]
            p = p - 1
        T[p] = v

def afficher(T, n):
    for i in range(n):
        print(T[i], end="   ")
    print()

n = saisir(3, 20)
remplir(T, n)
tri(T, n)
afficher(T, n)