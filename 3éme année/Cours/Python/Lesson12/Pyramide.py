from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def Play():
    E = win.Einput.text()
    win.ListV.clear()
    
    if int(E) < 1 or int(E) > 9 or int(E) % 2 == 0:
        QMessageBox.critical(win, "Erreur", "E doit etre un nombre impair entre 1 et 9!")
    else:
        win.ListV.addItem(E)
        main(E)

def main(x):
    ok = True
    while ok:
        if verifDiv(x):
            ok = False
        else:
             x = ajouter(x)

def verifDiv(y):
    ok = True
    signe = True
    N = 0
    while ok:
        if len(y) < 3:
            ok = False
            o = y[:]
        else:
            o = y[len(y) - 4:]
            y = y[:len(y) - 4]
        if signe:
            N = N + int(o)
            signe = False
        else:
            N = N - int(o)
            signe = True
    return N % 7 == 0

def ajouter(y):
    C = 0
    for i in range(len(y)):
        C = C + int(y[i]) + 1
    C = C % 10
    ch = ""
    ch = str(C) + y + str(C)
    win.ListV.addItem(ch)
    return ch

def Annuler():
    win.Einput.clear()
    win.ListV.clear()

def Fermer():
    win.close()

app = QApplication([])
win = loadUi("interface.ui")
win.show()
win.BtnF.clicked.connect(Play)
win.BtnA.clicked.connect(Annuler)
win.BtnQ.clicked.connect(Fermer)
app.exec_()