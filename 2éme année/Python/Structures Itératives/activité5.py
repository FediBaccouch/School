ch = str(input("donner une chaine: "))
c1 = str(input("donner le caractére à rechercher: "))
c2 = str(input("donner le nouveau caractére: "))
ch1 = ""

for i in range(0, len(ch)):
    if ch[i] == c1:
        ch1 += c2
    else:
        ch1 += ch[i]
print(ch1)