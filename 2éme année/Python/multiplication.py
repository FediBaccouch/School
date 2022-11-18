from abc import abstractclassmethod


n = int(input("donner un entier"))
for i in range(21):
    print(i, "X", n, "=", i*n)