def inverte(vet, n):
    b = n* [0]     

    cont1 = (n-1)
    cont2 = 0
    while cont1 >= 0:
        b[cont2] = vet[cont1]
        cont1 -= 1
        cont2 += 1
    return b
