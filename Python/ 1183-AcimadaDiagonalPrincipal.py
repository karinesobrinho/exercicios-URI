M = [[0 for i in range (12)] for j in range (12)]

O = input()
R = 0

for i in range (12):
  for j in range (12):
    M[i][j] = float(input())

if O == "S":
  for i in range (len(M)):
    for j in range (i+1, len(M[0])):
      R += M[i][j]
            

else:
  for i in range (len(M)):
    for j in range (i+1, len(M[0])):
      R += (M[i][j])/66
    

print ("%.1f"%R)