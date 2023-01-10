from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def Program():
    A = win.AInput.text()
    B = win.BInput.text()
    win.Output.setText("")
    if A.isdecimal() == False or int(A) < 1:
        win.Output.setText("A doit etre positive")
    elif B.isdecimal() == False or int(A) < 1:
        win.Output.setText("B doit etre positive")
    else:
        win.PPCMInput.setText(str(PPCM(int(A), int(B))))
        win.PGCDInput.setText(str(PGCD(int(A), int(B))))
        win.PUISSInput.setText(str(PUISS(int(A), int(B))))
        if PGCD(int(A), int(B)) == 1:
            win.Output.setText(f"{A} et {B} sont premiers etre eux")

def PPCM(A, B):
    x = A
    while x % B > 0:
        x += A
    return x

def PGCD(A, B):
    while B != 0:
        r = B % A
        A = B
        B = r
    return A

def PUISS(A, B):
    P = 1
    for i in range(1, B + 1):
        P *= A
    return P

app = QApplication([])
win = loadUi("interface.ui")
win.show()
win.CalculerBtn.clicked.connect(Program)
app.exec_()
