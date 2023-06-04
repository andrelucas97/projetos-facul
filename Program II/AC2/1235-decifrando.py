N = int(input())

for i in range(N):
    x = input()

    cont = int(len(x)/2)
    fraseDecifrada = ""

    while cont > 0:
        fraseDecifrada = fraseDecifrada + x[(cont-1)]
        cont -= 1
    cont2 = len(x)
    while cont2 > (len(x)/2):
        fraseDecifrada = fraseDecifrada + x[(cont2-1)]
        cont2 -= 1

    print(fraseDecifrada)
