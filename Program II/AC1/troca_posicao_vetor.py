N = []

for i in range (20):
    valor = int(input())
    N.append(valor)

for j in range (10):
    trocaValor = N[j]
    N[j] = N[(20-1)-j]
    N[20-1-j] = trocaValor
    
for x in range (20):
    print("N[%i] = %i" % (x, N[x]))

# N[i], N[20-1-i]
