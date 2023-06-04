from math import sqrt

def funcao():
    n = float(input())

    if n >= 0:
        valor = sqrt (n)
    else:
        valor = n **2
    print(valor)

