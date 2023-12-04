from numpy import array

T = array([int()] * 20)

def saisir(d, f):
  N = int(input("Donner N:  "))
  while N < d or N > f:
    N = int(input("Donner N:  "))
  return N

def remplir(T, N):
  for i in range(N):
    T[i] = int(input("Donner T[" + str(i) + "] = "))

def tri(T, N):
  permut = True
  while permut:
    permut = False
    for i in range(N - 2):
      if T[i] > T[i + 1]:
        aux = T[i]
        T[i] = T[i + 1]
        T[i + 1] = aux
        permut = True

def recherche(T, x, d, f):
  p1 = (2 * d + f) // 3
  p2 = (d + 2 * f) // 3
  if d > f:
    return False
  elif T[p1] == x or T[p2] == x:
    return True
  elif T[p1] > x:
    return recherche(T, x, d, p1 - 1)
  elif T[p2] > x:
    return recherche(T, x, p1 + 1, p2 - 1)
  else:
    return recherche(T, x, p2 + 1, f)


# PP
N = saisir(3, 20)
remplir(T, N)
tri(T, N)
x = int(input("Donner x: "))
print(recherche(T, x, 0, N))