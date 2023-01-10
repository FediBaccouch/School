from numpy import *

T = array([float] * 5)

for i in range(0, 5):
    T[i] = float(input("donner un reél: "))

max = T[0]
pos = 0

for i in range(1, 5):
    if T[i] > max:
        max = T[i]
        pos = i

print(str(max) + "-" + str(pos + 1))