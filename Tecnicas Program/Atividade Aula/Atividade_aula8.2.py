lista = []
num = 0

while num != -1:
    num = float(input())
    if num != -1:
        lista.append(num)


def ocorrencias(lst, x):
    n = len(lista) #lenght = tamanho
    cont1 = 0
    rep = 0
    while cont1 < n:
        if ( lista[cont1] == x):
            rep += 1
        cont1 += 1
        
    return rep

"""
ou use string.count('a')
"""

