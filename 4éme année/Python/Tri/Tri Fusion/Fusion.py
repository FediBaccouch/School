from numpy import array

def remplir(T, N):
  T[0] = int(input("Donner T[0] = "))
  for i in range(1, N):
    T[i] = int(input("Donner T[" + str(i) + "] = "))
    while T[i] < T[i - 1]:
      T[i] = int(input("Donner T[" + str(i) + "] = "))
  print()

def fusion(T, T1, T2, N, N1, N2):
  i = 0
  j = 0
  k = 0

  while i < N1 and j < N2:
    if T1[i] < T2[j]:
      T[k] = T1[i]
      i = i + 1
      k = k + 1
    else:
      T[k] = T2[j]
      j = j + 1
      k = k + 1
  
  while i < N1:
    T[k] = T1[i]
    i = i + 1
    k = k + 1
  
  while j < N2:
    T[k] = T2[j]
    j = j + 1
    k = k + 1

def afficher(T, N):
  for i in range(N):
    print(T[i], end='\t')
  print()

N1 = int(input("Donner N1: "))
N2 = int(input("Donner N2: "))

T = array([int()] * (N1 + N2))
T1 = array([int()] * N1)
T2 = array([int()] * N2)

remplir(T1, N1)
remplir(T2, N2)
fusion(T, T1, T2, N1 + N2, N1, N2)
afficher(T, N1 + N2)