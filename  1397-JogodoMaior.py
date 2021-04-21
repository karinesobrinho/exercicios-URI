while 1: 
  N = int(input())
  if N==0: break
  
  p1 = 0
  p2 = 0

  for i in range (N):
    A,B= input().split()
    A = int (A)
    B = int (B)
  
    if A>B: p1 += 1
    elif B>A: p2 += 1

  print (p1, p2)