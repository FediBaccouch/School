from numpy import *

def saisir(b1, b2):
    N = int(input("donner N: "))
    while N < b1 or N > b2:
        N = int(input("donner N: "))
    return N

def remplir(T, N):
    for i in range(N):
        T[i] = dict()
        T[i]["nom"] = input("donner le nom: ")
        T[i]["prenom"] = input("donner le prenom: ")
        T[i]["moy"] = float(input("donner le moy: "))
        while not (0 <= T[i]["moy"] <= 20):
            T[i]["moy"] = float(input("donner le moy: "))

def afficher(T, N):
    max = 0
    for i in range(1, N):
        if T[i]["moy"] > T[max]["moy"]:
            max = 1
    print(T[max])

N = saisir(3, 20)
T = array([dict()] * N)
remplir(T, N)
afficher(T, N)