a = float(input("a= "))
b = float(input("b= "))
op = str(input("operateur? "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("erreur")
    else:
        print(a / b)
else:
    print("opération impossible")