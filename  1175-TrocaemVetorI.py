lista = []
for i in range(20):    
    valor = int(input())
    lista.append(valor)
p = 0
for l in lista[::-1]:
    print("N[%d] = %d" %(p,l))
    p += 1