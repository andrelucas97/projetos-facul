N = int(input())
for i in range(N):
    x = input()
    a = []
    soma = 0
    for i in x.split():
        a.append(i)
    tam = len(a[0])
    tam2 = len(a[1])

    if tam < tam2:
        print('nao encaixa')
    else:
        y = 0
        for j in range((tam-tam2),tam):
            if a[0][j] == a[1][y]:
                soma += 1
            y += 1
        if soma == tam2:
            print('encaixa')
        else:
            print('nao encaixa')
