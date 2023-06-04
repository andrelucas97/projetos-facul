qtd_alunos = int(input("Informe a quantidade de alunos: "))

valor = 0
trab = 5
notas = []

for i in range(qtd_alunos):
    linha = [valor] * trab
    notas.append(linha)

cont1 = 0
for cont1 in range(qtd_alunos): 
    aluno = input('informe o nome do aluno: ')
    media = 0
    soma = 0
    maior_aluno = aluno
    maior_media = media
    
    for cont2 in range(trab):         
        valor = float(input('Informe a nota ' +str(cont2)+ ' do aluno: '))
        notas[cont1][cont2] = valor
        soma += valor
        cont2 += 1
    for cont3 in range (trab):
        print('Nota', (cont3+1), ':', notas[cont1][cont3])        
    
    media = soma/trab
    print('Média: ', media)
    
    print() # para pular linha
    if media > maior_media:
        maior_media = media
        maior_aluno = aluno
    
    cont1 += 1
    
print('O aluno', aluno, 'possui a maior média:', media)

