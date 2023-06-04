while True:
    try:
        N = input()

        if N == '':
            break
        else:
        
            lista = []
            for i in range(int(N)):
                tel = input()
                lista.append(tel)
            soma = 0
            lista.sort()
            for j in range(1,int(N)):
                for comp in range(len(lista[0])):
                    if lista[j-1][comp] != lista[j][comp]:
                        break
                    else:
                        soma += 1

            print(soma)
                    

        
    except EOFError:
        break
