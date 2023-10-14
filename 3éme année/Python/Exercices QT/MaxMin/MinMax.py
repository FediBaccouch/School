from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def Play():
    N = win.NInput.text()
    win.ErrorOutput.setText("")
    if N.isdecimal() == False or int(N) <= 9:
        win.ErrorOutput.setText("N doit etre un entier > 9")
    else:
        win.MaxOutput.setText(str(Max(N)))
        win.MinOutput.setText(str(Min(N)))

def Max(N):
    permut = True
    while permut:
        permut = False
        for i in range(len(N) - 1):
            if int(N[i]) < int(N[i + 1]):
                N = N[:i] + N[i + 1] + N[i] + N[i + 2:]
                permut = True
    return int(N)

def Min(N):
    permut = True
    while permut:
        permut = False
        for i in range(len(N) - 1):
            if int(N[i]) > int(N[i + 1]):
                N = N[:i] + N[i + 1] + N[i] + N[i + 2:]
                permut = True
    return int(N)

app = QApplication([])
win = loadUi("MinMax.ui")
win.show()
win.CalculerBtn.clicked.connect(Play)
app.exec_()