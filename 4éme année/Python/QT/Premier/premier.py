from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def Play():
  a = win.aa.text()
  b = win.bb.text()
  win.outputList.clear()
  if not a.isdecimal() or int(a) not in range(10, 100):
    QMessageBox.critical(win, "erreur", "A doit etre un entier entre 10 et 99")
  elif not b.isdecimal() or int(b)not in range(int(a), 10001):
    QMessageBox.critical(win, "erreur", "B doit etre un entier entre " + a + "et 10000")
  else:
    for i in range(int(a), int(b) + 1):
      if supPremier(i):
        win.outputList.addItem(str(i))
    win.aa.clear()
    win.bb.clear()

def premier(x):
  test = True
  for i in range(2, x):
    if x % i == 0:
      test = False
  return test

def supPremier(n):
  while premier(n) and n > 10:
    n = n // 10
  return premier(n)

app = QApplication([])
win = loadUi("interface.ui")
win.show()
win.premierButton.clicked.connect(Play)
app.exec_()