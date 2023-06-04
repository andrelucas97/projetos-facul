a = []
N = int(input())
valor = input()


for i in valor.split():
    a.append(float(i))
    
menor_valor = a[0]
posicao = 0

for j in range (N):
    if a[j] < menor_valor:
        menor_valor = a[j]
        posicao = j
print('Menor valor: %i' % menor_valor)
print('Posicao:', posicao)
