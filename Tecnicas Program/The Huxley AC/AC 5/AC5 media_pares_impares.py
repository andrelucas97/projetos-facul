def media_pares_impares(lista):
    n = len(lista)
    par = 0
    impar = 0
    media1 = 0
    media2 = 0
    for i in range(n):
        if lista[i]%2 == 0:
            par += lista[i]
            media1 += 1
        else:
            impar += lista[i]
            media2 += 1
    print(par/media1)
    print(impar/media2)



lista = eval(input())
media_pares_impares(lista)

