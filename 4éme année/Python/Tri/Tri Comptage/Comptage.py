from numpy import array

T = array([int()] * 100)
T1 = array([int()] * 100)

def remplir(T, N):
  c = 0
  T[0] = int(input("Donner T[0] = "))
  for i in range(1, N):
    test = False
    while not test:
      test = True
      x = int(input("Donner T[" + str(i) + "] = "))
      j = 0
      while j < N and test:
        if x == T[j]:
          test = False
        j = j + 1
      T[i] = x

def comptage(T, T1, N):
  for i in range(N):
    c = 0
    for j in range(N):
      if T[j] < T[i]:
        c = c + 1
    T1[c] = T[i]

def afficher(T1, N):
  for i in range(N):
    print(T1[i], end="\t")
  print()

N = int(input("Donner N: "))

remplir(T, N)
comptage(T, T1, N)
afficher(T1, N)