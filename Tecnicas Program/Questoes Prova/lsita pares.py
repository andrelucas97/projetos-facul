matriz = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16] ]
qtd_lin = len(matriz)
qtd_col = len(matriz[0])
lista = []
for i in range(qtd_lin):
    for j in range(qtd_col):
        if (i % 2) == 0 and (j % 2) == 0:
            lista.append(matriz[i][j])

print(lista)
