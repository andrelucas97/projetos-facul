i = 0

while True:
    try:
        x = input()

        if x == "":
            break

        if i > 0:        
            print()
            
        i += 1

        lista = {}

        for i in range(len(x)):
            y = ord(x[i])
            lista[y] = lista.get(y, 0) + 1 

        for item in sorted(lista, key = lista.get):
            print (item, lista[item])
        '''
        listOrdenada = {k:v for k, v in sorted(lista.items(), key=lambda item: (item[1], -item[0]))}

        for saida in listaOrdenada:
            print('%i %i' % (saida, listaOrdenada[saida]))'''

    except EOFError:
        break

