def cria_matriz(m, n, valor):
    matriz = []
    for i in range (m):
        linha = [valor] * n
        matriz.append(linha)
    return matriz

m = int(input('Informe a quantidade de alunos:'))
n = 6 # colunas
matriz = cria_matriz(m, n, 0)

for i in range(m):
    matriz[i][0] = input("Informe o nome do aluno " +str(i)+ ": ")
    for j in range(1, n): #j varia de 1 a n-1
        matriz[i][j] = float(input("Informe a nota " +str(j)+ " do aluno " +str(i)+ ": "))
    print()
print("\nPercorrendo a matriz: \n")

maior_media = -1
pos_maior = -1

for i in range(m):
    print("Aluno:", matriz [i][0])
    soma = 0
    for j in range(1, n):
        print("Nota", j, ": ", matriz[i][j])
        soma = soma + matriz[i][j]
    media = soma / (n-1)
    print("Média:", media)
    print()
    if media > maior_media:
        maior_media = media
        pos_maior = i
print()
print("O aluno", matriz[pos_maior][0], "possui a maior média:", maior_media)
