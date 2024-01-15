from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def Play1():
  a = win.aa.text()
  b = win.bb.text()
  if not a.isdecimal() or int(a) < 1 or a == "":
    QMessageBox.critical(win, "erreur", "A invalide!")
  if not b.isdecimal() or int(b) < 1 or b == "":
    QMessageBox.critical(win, "erreur", "B invalide!")
  else:
    for i in range(int(a), int(b) + 1):
      if not premier(i):
        win.l1.addItem(str(i))

def Play2():
  a = win.aa.text()
  b = win.bb.text()
  if not a.isdecimal() or int(a) < 1 or a == "":
    QMessageBox.critical(win, "erreur", "A invalide!")
  if not b.isdecimal() or int(b) < 1 or b == "":
    QMessageBox.critical(win, "erreur", "B invalide!")
  else:
    for i in range(int(a), int(b) + 1):
      if isRigolos(i):
        win.l2.addItem(facteurPremier(i))

def isRigolos(x):
  xx = x
  S = 0
  i = 2
  while i < (x // 2) + 1 and xx != 1:
    print(i)
    if xx % i == 0:
      for j in range(len(str(i))):
        S = S + int(str(i)[j])
      xx = xx // i
    else:
      i = i + 1
  xx = 0
  for i in range(len(str(x))):
    xx = xx + int(str(x)[i])
  print(xx)
  print(S)
  return S == xx

def facteurPremier(x):
  xx = x
  ch = ""
  i = 2
  while i < x and xx != 1:
    if xx % i == 0:
      ch = ch + str(i) + "*"
      xx = xx // i
    else:
      i = i + 1
  ch = ch[:-1]
  return str(x) + "= " + ch

def premier(x):
  test = True
  for i in range(2, x):
    if x % i == 0:
      test = False
  return test

def Reset():
  win.aa.clear()
  win.bb.clear()
  win.l1.clear()
  win.l2.clear()

def Exit():
  win.close()

app = QApplication([])
win = loadUi("interface.ui")
win.show()
win.btn1.clicked.connect(Play1)
win.btn2.clicked.connect(Play2)
win.btn3.clicked.connect(Reset)
win.btn4.clicked.connect(Exit)
app.exec_()