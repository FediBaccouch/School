from numpy import *

T = array([int()] * 5)

T[0] = 15
T[1] = 10
T[2] = -1
T[3] = 7
T[4] = -2

def trierInsertion():
    for i in range(1, 5):
        x = T[i]
        j = i
        while (x < T[j - 1]) and (j > 0):
            T[j] = T[j - 1]
            j -= 1
        T[j] = x


trierInsertion()
for i in range(5):
    print(T[i])