def interseccao(lista1, lista2):
    cont2 = 0
    cont1 = 0

    if len(lista1)> len(lista2):

        lista_maior = lista1
        lista_menor = lista2
    else:

        lista_maior = lista2
        lista_menor = lista1
    listaf = []
    for i in range(len(lista_menor)):        
        for j in range(len(lista_maior)):
            if lista_menor[i] == lista_maior[j]:
                listaf.append(lista_menor[i])
    listaf.sort()
    for i in range(len(listaf)-1,0,-1):
        if listaf[i] == listaf[i-1]:
            del listaf[i]
    return listaf

lista1 = eval(input())
lista2 = eval(input())

resultado = interseccao(lista1, lista2)
if isinstance(resultado, list):
    print(resultado)
else:
    print("Erro. Voce deve devolver uma lista")
