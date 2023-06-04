import time

nome = input('Nome do arquivo? ')
palavra = input('Palavra? ')

f = open(nome, 'r')
i = 1
for linha in f.readlines():
    if palavra in linha:
        print('Linha', i, ':')
        print(linha)
    i += 1
    
f.close()
