n = str(input("quel est le numéro: "))

if len(n) != 8:
    print("inexistant")
elif n[0] == "9":
    print("télecom")
elif n[0] == "2":
    print("ooredoo")
elif n[0] == "5":
    print("orange")
elif n[0] == "7":
    print("fixe")
else:
    print("inexistant")