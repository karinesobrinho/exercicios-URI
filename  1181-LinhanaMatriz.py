M = [[0 for j in range(0,12)] for i in range(0,12)]

#N = [0]*12
#for i in range(0,12):
#  N[i] = [0]*12
l = int(input())
c = input()
for i in range(0,12):
  for j in range(0,12):
    M[i][j] = float(input())

#for i in range(0,12):
#  print(M[i])

soma = 0
for j in range(0,12):
  soma = soma+M[l][j]

if c == "S":
  print("%.1f"%soma)
else:
  media = soma/12
  print("%.1f"%media)