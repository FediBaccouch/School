from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def Convertir():
    N = win.NInput.text()
    base = win.BaseInput.text()
    win.msg.clear()
    if N.isdecimal() == False or int(N) < 10:
        QMessageBox.critical(win, "Error", "N doit etre > 10")
    elif base.isdecimal() == False or 16 < int(base) < 2:
        QMessageBox.critical(win, "Error", "base doit etre < 16 et > 2")
    else:
        win.msg.setText(conversionBase(int(N), int(base)))

def Annuler():
    win.msg.clear()
    win.NInput.clear()
    win.BaseInput.clear()

def Fermer():
    win.close()

def conversionBase(N, B):
    ch = ""
    while N != 0:
        X = N % B
        N = N // B
        if X < 10:
            ch = str(X) + ch
        else:
            ch = chr(X + 55) + ch
    return ch

app = QApplication([])
win = loadUi("interface.ui")
win.show()
win.ConvertirBtn.clicked.connect(Convertir)
win.AnnulerBtn.clicked.connect(Annuler)
win.FermerBtn.clicked.connect(Fermer)
app.exec_()