from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def Play():
    N = win.inputN.text()
    win.res.setText("")
    if N.isdecimal() == False:
        win.res.setText("donnée non acceptable")
    elif verifier(int(N)):
        win.res.setText(f"{N} vérifie cette propriété")
    else:
        win.res.setText(f"{N} ne vérifie pas cette propriété")

def verifier(N):
    S = 1
    for i in range(2, (N // 2) + 2):
        if N % i == 0:
            S *= i
    return S == N

app = QApplication([])
win = loadUi("propriete.ui")
win.show()
win.btn.clicked.connect(Play)
app.exec_()