from numpy import *

E = dict(ch = "", chy = "")
TabE = array([E] * 15)
Tab = array([str] * 15)
Mat = array([[str] * 15] * 15)

def saisir(a, b):
    n = int(input("donner n: "))
    while n < a or n > b:
        n = int(input("donner n: "))
    return n

def remplir(Tab, n):
    for i in range(n):
        Tab[i] = str(input("donner une chaine: "))
        while len(Tab[i]) < 3:
            Tab[i] = str(input("donner une chaine de longueur ≥ 3 : "))

def affichage(TabE, n):
    print("")  # pour que l'affichage fasse un espace entre les données d'utilisateur et les données d'affichage
    for i in range(n):
        print(TabE[i]["ch"])
        print(TabE[i]["chy"])
        print("------------")  # pour que l'affichage fasse un espace entre les différentes données d'enregistrement

def construit(TabE, Tab, n):
    for i in range(n):
        ch = espace(Tab[i])
        chy = cryptage(ch)
        TabE[i] = {}
        TabE[i]["ch"] = Tab[i]
        TabE[i]["chy"] = chy

def espace(ch):
    while len(ch) % 3 != 0:
        ch += " "
    return ch

def cryptage(ch):
    k = 0
    for i in range(len(ch) // 3):
        for j in range(3):
            Mat[i, j] = ch[k]
            k += 1
    for x in range(3):
        Tri(Mat, len(ch) // 3, x)
    ch1 = ""
    for i in range(len(ch) // 3):
        for j in range(3):
            ch1 += Mat[i, j]
    return ch1

def Tri(Mat, n, x):
    permut = True
    while permut:
        permut = False
        for i in range(n - 1):
            if Mat[i, x] > Mat[i + 1, x]:
                temp = Mat[i, x]
                Mat[i, x] = Mat[i + 1, x]
                Mat[i + 1, x] = temp
                permut = True

n = saisir(3, 15)
remplir(Tab, n)
construit(TabE, Tab, n)
affichage(TabE, n)