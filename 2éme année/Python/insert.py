n = int(input("donner n: "))
c = int(input("donner c: "))

s = (n // 10) * 100 + c * 10 + n % 10

print(s)