'''
Crie uma funçao que receba como parametro um vetor
vet e o seu tamanho n. A função deverá inverter
a sequencia de itens de vet, sem usar um vetor
auxiliar
'''
def exibe(v, n):
    for i in range(n):
        print(v[i], end= ' ')
    print()

def troca(v, i, j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp

def inverte(vet, n):
    j = n-1
    i = 0
    while i < j:
        troca(vet, i, j)
        i += 1
        j -= 1


a = [10, 20, 30, 40, 50]
exibe(a, 5)
inverte(a, 5)
exibe(a, 5)
