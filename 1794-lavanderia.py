N = int(input())

la,lb= input().split()
la = int (la)
lb = int (lb)

sa,sb= input().split()
sa = int (sa)
sb = int (sb)

if sa <= N <= sb and la <= N <= lb:
  print("possivel")
else:
  print("impossivel")