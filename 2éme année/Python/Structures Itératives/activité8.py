from numpy import *

T = array([float] * 5)

for i in range(0, 5):
    T[i] = float(input("donner un réel: "))

s = 0

for i in range(0, 5):
    s += T[i]
    print(T[i])

print(s)