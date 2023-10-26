from numpy import array

M = array([[int()] * 30] * 20)
Mmin = array([[int()] * 30] * 20)
Mmax = array([[int()] * 30] * 20)

def saisir(bi, bs, msg):
    x = int(input(msg))
    while x < bi or x > bs:
        x = int(input(msg))
    return x

def remplir(M, L, C):
    for i in range(L):
        for j in range(C):
            M[i, j] = int(input("M[" + str(i) + ", " + str(j) + "]= "))
            while M[i, j] < 1:
                M[i, j] = int(input("M[" + str(i) + ", " + str(j) + "]= "))

def remplir1(Mmin, Mmax, M, nl, nc):
    for i in range(nl):
        for j in range(nc):
            if mini(M, M[i, j], i, nc):
                Mmin[i, j] = 1
            if maxi(M, M[i, j], j, nl):
                Mmax[i, j] = 1

def mini(M, x, L, nc):
    test = True
    for i in range(nc):
        if M[L,i] < x:
            test = False
    return test

def maxi(M, x, C, nl):
    test = True
    for i in range(nl):
        if M[i, C] > x:
            test = False
    return test

def former(F, M, Mmin, Mmax, L, C):
    for i in range(L):
        for j in range(C):
            if Mmin[i, j] == 1 and Mmax[i, j] == 1:
                F.write(str(M[i, j]) + " (" + str(i + 1) + "," + str(j + 1) + ")" + "\n")
    F.close()

def afficher(F):
    F = open("resultat.txt", "r")

    x = F.readline()

    while x != "":
        x = x[0: len(x) - 1]
        print(x)
        x = F.readline()
    F.close()

L = saisir(5, 30, "nbre lignes: ")
C = saisir(3, 20, "nbre collones: ")
remplir(M, L, C)
remplir1(Mmin, Mmax, M, L, C)
F = open("resultat.txt", "w")
former(F, M, Mmin, Mmax, L, C)
afficher(F)