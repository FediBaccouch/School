n = float(input("donner un réel: "))
max = n
min = n

for i in range(2, 51):
    n = float(input("donner un réel: "))
    if n > max:
        max = n
    if n < min:
        min = n

print(min, max)