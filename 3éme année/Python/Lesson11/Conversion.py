from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def Play():
    inp = win.bb.text()
    win.msg.setText("")
    if len(inp) == 0 or not inp.isdecimal() or not verif(inp):
        QMessageBox.critical(win, "Erreur", "A doit etre un entier 0 ou 1!")
    elif win.r1.isChecked():
        win.msg.setText(str(Octal(inp)))
    elif win.r2.isChecked():
        win.msg.setText(str(Hexa(inp)))
    else:
        QMessageBox.critical(win, "Erreur", "Choisir une option svp!")

def Annuler():
    win.bb.clear()
    win.msg.clear()
    win.r1.setAutoExclusive(False)
    win.r1.setChecked(False)
    win.r2.setAutoExclusive(False)
    win.r2.setChecked(False)

def Fermer():
    win.close()

def verif(N):
    correct = True
    i = -1
    while correct == True and i < len(N) - 1:
        i += 1
        if N.isdecimal() == False and ord(N[i]) - 55 >= 2:
            correct = False
        elif int(N[i]) >= 2:
            correct = False
    return correct

def conv(n, k):
    s = 0
    chc = ""
    for i in range(len(n)):
        z = puissance(k, len(n) - 1 - i)
        s += (int(n[i]) * z)
        if s > 9:
            chc = chr(55 + s)
        else:
            chc = str(s)
    return str(chc)

def Octal(n):
    while len(n) % 3 != 0:
        n = "0" + n
    s = ""
    for i in range(0, len(n), 3):
        ch = n[i:i+3]
        c = conv(ch, 2)
        s += c
    return s

def Hexa(n):
    while len(n) % 4 != 0:
        n = "0" + n
    s = ""
    for i in range(0, len(n), 4):
        ch = n[i:i+4]
        c = conv(ch, 2)
        s += c
    return s

def puissance(x, y):
    k = 1
    for i in range(1, y + 1):
        k *= x
    return k

app = QApplication([])
win = loadUi("interface.ui")
win.show()
win.btn.clicked.connect(Play)
win.btna.clicked.connect(Annuler)
win.btnq.clicked.connect(Fermer)
app.exec_()