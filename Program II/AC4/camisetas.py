i = 0
while True:
    N = int(input())

        
    if N == 0:
        break
    
    if i > 0:
        print()
    
    lista = []

    for i in range(N):
        lista.append([0] * 3)

    for i in range(N):
        nome = input()
        lista[i][0] = nome
                
        camisa = input().split()
        lista[i][1] = camisa

        if lista[i][1][1] == 'P':
            lista[i][2] = 'A'
        elif lista[i][1][1] == 'M':
            lista[i][2] = 'B'
        elif lista[i][1][1] == 'G':
            lista[i][2] = 'C'


    lista.sort(key = lambda k:k[1][0] + k[2] + k[0])


    for x in range(len(lista)):
        print('%s %s %s' % (lista[x][1][0], lista[x][1][1], lista[x][0]))

    
