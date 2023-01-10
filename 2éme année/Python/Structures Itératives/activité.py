from numpy import *
from random import *

nom = array([str] * 10)
nombre = array([int] * 10)

for i in range(0, 10):
    nom[i] = str(input("donner votre nom: "))
    nombre[i] = randint(0, 51)

max = nombre[0]
gagnant = nom[0]

for i in range(1, 10):
    if nombre[i] > max:
        max = nombre[i]
        gagnant = nom[i]

print(gagnant + "-" + str(max))