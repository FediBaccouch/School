from numpy import *

m = array([float] * 25)

for i in range(0, 25):
    m[i] = float(input("donner la moyenne: "))

s = 0

for i in range(0, 25):
    s += m[i]

moy = s / 25
print(moy)