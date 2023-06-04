# quando x não está em vet, retorna -1
def indice (vet, x, n):
    for i in range(n):
        if vet[i] == x:
            return i
    return -1
