n = int(input("donner n: "))

c = n // 100
x = n % 100
d = x // 10
u = x % 10
inv = u * 100 + d * 10 + c

print(inv)