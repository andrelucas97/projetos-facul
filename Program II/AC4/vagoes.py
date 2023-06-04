def mergeSort(X, n):
    lista = [0]*n
    return mergeSort1(X, lista, 0, n-1)

def mergeSort1(X, lista, esq, direita):
    count1 = 0
    if esq < direita:
        meioLista = (esq+direita)//2
        count1 += mergeSort1(X, lista, esq, meioLista)
        count1 += mergeSort1(X, lista, meioLista + 1, direita)
        count1 += merge(X, lista, esq, meioLista, direita)
    return count1

def merge(X, lista, esq, meioLista, direita):
    i = esq
    j = meioLista + 1
    k = esq
    count1 = 0
    while i <= meioLista and j<= direita:
        if X[i] <= X[j]:
            lista[k] = X[i]      

            k += 1
            i += 1
            
        else:
            lista[k] = X[j]
            count1 += (meioLista-i + 1)
            k += 1
            j += 1
    while i <= meioLista:
        lista[k] = X[i]
        k += 1
        i += 1
    while j <= direita:
        lista[k] = X[j]
        k += 1
        j += 1

    for loop_var in range (esq, direita + 1):
        X[loop_var] = lista[loop_var]
        
    return count1

vezes = int(input())
for i in range(vezes):
    tam = int(input())
    trens = list(map(int, input().split()))
    x = mergeSort(trens,tam)

    print('Optimal train swapping takes %i swaps.' %x)
        



































'''N = int(input())

for z in range(N):
    soma = 0
    x = int(input())

    y = input().split()

    for i in range(1, x):
        j = i
        while j > 0 and y[j] < y[j-1]:
            y[j], y[j-1] = y[j-1], y[j]
            soma += 1
            j -= 1
    print('Optimal train swapping takes %i swaps' % soma)'''
