L,C = input().split()
A,B = input().split()
A = int(A) - 1
B = int(B) - 1
C = int(C)
L = int(L)
M = []
s = 1
for i in range(L):
  M.append(input().split())
  for j in range(C):
    M[i][j] = int(M[i][j])
while s == 1:
  M[A][B] = 0
  if B < C-1 and M[A][B+1] == 1:
    B += 1
  elif B > 0 and M[A][B-1] == 1:
    B -= 1
  elif A < L-1 and M[A+1][B] == 1:
    A += 1
  elif A > 0 and M[A-1][B] == 1:
    A -= 1
  else:
    A += 1
    B += 1
    s = 0
print(A,B)