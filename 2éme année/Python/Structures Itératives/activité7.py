n = int(input("donner un entier: "))

for i in range(1, n):
    if n % i == 0:
        print(i)
