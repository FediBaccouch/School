from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def Convertir():
    N = win.NInput.text()
    base = win.BaseInput.text()
    win.msg.clear()
    if test(N, int(base)) == False:
        QMessageBox.critical(win, "Error", "N n'est pas compatible avec le base")
    elif base.isdecimal() == False or 16 < int(base) < 2:
        QMessageBox.critical(win, "Error", "base doit etre < 16 et > 2")
    else:
        win.msg.setText(conversionBase(N, int(base)))

def Annuler():
    win.msg.clear()
    win.NInput.clear()
    win.BaseInput.clear()

def Fermer():
    win.close()

def test(N, B):
    correct = True
    i = -1
    while correct == True and i < len(N) - 1:
        i += 1
        if N.isdecimal() == False and ord(N[i]) - 55 >= B:
            correct = False
        elif int(N[i]) >= B:
            correct = False
    return correct

def conversionBase(N, B):
    S = 0
    for i in range(len(N)):
        if N[i] <= "9":
            S += int(N[i]) * puissance(B, len(N) - 1 - i)
        else:
            S += (ord(N[i]) - 55) * puissance(B, len(N) - 1 - i)
    return str(S)

def puissance(x, y):
    P = 1
    for i in range(1, y + 1):
        P *= x
    return P

app = QApplication([])
win = loadUi("interface.ui")
win.show()
win.ConvertirBtn.clicked.connect(Convertir)
win.AnnulerBtn.clicked.connect(Annuler)
win.FermerBtn.clicked.connect(Fermer)
app.exec_()