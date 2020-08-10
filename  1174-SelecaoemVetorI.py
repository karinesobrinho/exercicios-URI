A = [0]*100

for i in range (100):
  A[i] = float(input())
  
for i in range (100):
  if A[i]<=10:
    print ("A["+str(i)+"] =",A[i])