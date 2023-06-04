maior_lido = 0
pos_maior = 0

for i in range(1,6+1):
    valor = int(input())
    if valor > maior_lido:
        maior_lido = valor
        pos_maior = i

print(maior_lido)
print(pos_maior)
