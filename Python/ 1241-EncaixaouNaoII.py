q = int(input())

for i in range(q):
    A, B = list(map(str,input().split()))
    if A[-len(B):] == B:
        print("encaixa")
    else:
        print("nao encaixa")