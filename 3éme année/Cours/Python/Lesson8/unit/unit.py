from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def Play():
    N = win.inputN.text()
    win.aff.setText("")
    if N.isdecimal() == False:
        win.aff.setText("donnée non valide")
    elif verifier(int(N)):
        win.aff.setText("c'est un nombre unitairement parfait")
    else:
        win.aff.setText("n'est pas nombre unitairement parfait")

def verifier(N):
    S = 0
    for i in range(1, (N // 2) + 1):
        if N % i == 0 and premier(i, N // i):
            S += i
    return N == S

def premier(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a == 1

app = QApplication([])
win = loadUi("unitp.ui")
win.show()
win.btn.clicked.connect(Play)
app.exec_()