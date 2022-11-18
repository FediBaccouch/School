essai = 1
mdp = input("donner mdp: ")

while essai < 3:
    if mdp == "soleil":
        break
    else:
        essai += 1
        mdp = input("donner mdp: ")

if mdp == "soleil":
    print("Bienvenue")
else:
    print("incorrect")