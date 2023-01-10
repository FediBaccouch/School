from numpy import *

T = array([int] * 25)

for i in range(0, 25):
    T[i] = int(input("donner un entier: "))

x = int(input("donner x: "))

n = 0

for i in range(0, 25):
    if T[i] == x:
        n += 1

print(n)