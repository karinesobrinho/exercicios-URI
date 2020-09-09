n = int(input())

def uri(n):
  x = 0
  B = []
  A = [[0 for i in range(n)] for j in range(n)]
  for i in range(len(A)):
      A[i] = input().split(' ')

  
  while x < 2*n:
    lista = []
    lista = input().split(" ")
    i = 0
    j = i+1
    i = int(lista[i])-1
    j = int(lista[j])-1
    if A[i][j] not in B:
      B.append(A[i][j])
    x+=1
    i+=1
  return len(B)


print(uri(n))