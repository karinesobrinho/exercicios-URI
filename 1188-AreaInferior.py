O = input()
m,n = 12,12
s = 0
M = [[0 for j in range(n)] for i in range(m)]
for i in range(m):
  k = 11
  for j in range(n):
    M[i][j] = float(input())
    if i > j and k - j < i:
      s += M[i][j]
if O == "M":
  s = s / 66
print ("%.1f" %s)
