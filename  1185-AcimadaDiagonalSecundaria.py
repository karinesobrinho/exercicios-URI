M = [[0 for i in range (12)] for j in range (12)]

O = input()
R = 0

for i in range (12):
  for j in range (12):
    M[i][j] = float(input())

if O == "S":
  for i in range (len(M)):
    for j in range (len(M[0])-(i+1)):
      R += M[j][i]

else:
  for i in range (len(M)):
      for j in range (len(M[0])-(i+1)):
        R += (M[j][i])/66
      

print ("%.1f"%R)