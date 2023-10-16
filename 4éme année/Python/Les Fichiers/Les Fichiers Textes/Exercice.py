def remplir(F, n):
    for i in range(n):
        ch = input("Donner ch: ")
        F.write(ch + "\n")
    F.close()

def afficher(F):
    F = open("./phrases.txt", "r")
    ch = F.readline()
    while ch != "":
        ch = ch[:-1]
        if tauto(ch):
            print(ch, end="\n")
        ch = F.readline()
    F.close()

def tauto(ch):
    ch1 = ch.upper()
    t = True
    while ch.find(" ") != -1 and t:
        if ch[0] != ch[ch.find(" ") + 1]:
            t = False
        else:
            ch = ch[ch.find(" ") + 1:]
    return t

n = int(input("Donner n: "))
F = open("./phrases.txt", "w")
remplir(F, n)
afficher(F)