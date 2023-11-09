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
    p = 0
    while p < n:
        p = p * 3 + 1
    while p > 1:
        p = p // 3
        for i in range(p, n):
            v = T[i]
            j = i
            while T[j - p] > v and j >= p:
                T[j] = T[j - p]
                j = j - p
            T[j] = v

def afficher(T, n):
    for i in range(n):
        print(T[i], end="   ")
    print()

n = saisir(3, 20)
remplir(T, n)
tri(T, n)
afficher(T, n)