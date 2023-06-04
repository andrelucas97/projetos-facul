def cria_matriz(m, n, valor):
    matriz = []
    for i in range (m):
        linha = [valor] * n
        matriz.append(linha)
    return matriz

def le_csv(nome, separador, nCols):
    dados = []
    with open(nome, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.rstrip()
            linha = linha.split(',')
            for i in range(1, nCols):
                aluno[i] = float(aluno[i])
            dados.append(aluno)
    return dados
            
def grava_csv(nome, modo, dados, esquema, separador):
    with open(nome, modo) as arquivo:
        esquema = separador.join(esquema) + '\n'
        for linha in dados:
            arquivo.write(esquema % tuple(linha))

n = 6
nome_arquivo = 'aluno.csv'
opcao = input('Informe o modo de operação (C-carregar dados gravados / I - inserir dados novos): ')
if opcao.upper() == 'C': # opcao.upper transforma a string para caixa alta
    matriz = le_csv(nome_arquivo, ',', n)
    m = len(matriz)
else:
    m = int(input('Informe a quantidade de alunos: '))
    matriz = cria_matriz(m, n, 0)
    for i in range(m):
        matriz[i][0] = input('Informe o nome do aluno ' +str(i)+ ': ')
        for j in range(1, n): #j varia de 1 a n-1
            matriz[i][j] = float(input("Informe a nota " +str(j)+ " do aluno " +str(i)+ ": "))
        print()
    esquema = ['%s'] + ['%2f'] * (n-1)
    grava_csv(nome_arquivo, 'a', matriz, esquema, ',')
              
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

