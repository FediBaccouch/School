from numpy import *

Livre = dict(titre = "", code = 0, auteur = "", prix = 0.0)
n = 2
T = array([Livre] * n)

def verif_code(T, x):
    nb = 0
    for i in range(n):
        if T[i]["code"] == x:
            nb += 1
    ch = str(x)
    return (nb == 1) and len(ch) == 8

def remplir(T, n):
    for i in range(n):
        print("introduire les informations du livre n° ", i + 1)
        T[i] = {}
        T[i]["titre"] = str(input("donner titre: "))
        T[i]["code"] = int(input("donner code: "))
        while verif_code(T, T[i]["code"]) == False:
            T[i]["code"] = int(input("donner code: "))
        T[i]["auteur"] = str(input("donner auteur: "))
        T[i]["prix"] = float(input("donner prix: "))
    print("Remplissage terminé")

def rech_aff(T, n):
    print("")
    print("Recherché un livre par titre")
    titre_rech = str(input("donner le titre recherché: "))
    for i in range(n):
        if T[i]["titre"] == titre_rech:
            print("son code =", T[i]["code"])
            print("son auteur =", T[i]["auteur"])
            print("son prix =", T[i]["prix"])
    print("affichage terminé")

def modif_prix(T, n):
    print("")
    print("Modification du prix connaissant le code")
    coderech = int(input("donner le code à rechercher: "))
    i = 0
    while i < n and coderech != T[i]["code"]:
        i += 1
    if coderech == T[i]["code"]:
        nouv_prix = float(input("donner le nouveau prix: "))
        T[i]["prix"] = nouv_prix
        print("modification effectuée")
    else:
        print("ce code n'existe pas")

def nb_livres(T, n):
    nbl = 0
    for i in range(n):
        if auteur_rech == T[i]["auteur"]:
            nbl += 1
    return nbl

remplir(T, n)
rech_aff(T, n)
modif_prix(T, n)
auteur_rech = str(input("donner le nom de l'auteur recherché: "))
resultat = nb_livres(T, n)
print("")
print("le nombre de livre de ", auteur_rech, " = ", resultat)
