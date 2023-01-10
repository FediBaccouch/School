email = str(input("donner email: "))

if email.find("@") == -1 or email.find(".") == -1:
    x = 0
else:
    p1 = email.find("@")
    p2 = email.find(".")
    nom = email[0:p1]
    serveur = email[p1 + 1:p2]
    extension = email[p2 + 1:]
    if p2 < p1:
        x = 0
    elif len(email) < 15 or len(email) > 25:
        x = 0
    elif len(nom) < 1 or len(nom) > 15:
        x = 0
    elif len(serveur) < 1 or len(serveur) > 7:
        x = 0
    elif len(extension) < 1 or len(extension) > 3:
        x = 0
    else:
        x = 1

if x == 1:
    print("valid")
else:
    print("invalid")