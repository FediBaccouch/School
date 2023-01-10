from numpy import *

T = array([int()] * 5)

T[0] = 15
T[1] = 10
T[2] = -1
T[3] = 7
T[4] = -2

def trierBulle():
    permut = True
    while permut == True:
        permut = False
        for i in range(5 - 1):
            if T[i] > T[i + 1]:
                aux = T[i]
                T[i] = T[i + 1]
                T[i + 1] = aux
                permut = True


trierBulle()
for i in range(5):
    print(T[i])