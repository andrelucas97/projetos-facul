import os

nome1 = input('Arquivo entrada? ')
nome2 = input('Arquivo saida? ')
original = input('Palavra original? ')
alterada = input('Palavra alterada? ')

f1 = open(nome1, 'r')
f2 = open(nome2, 'w')

for linha in f1.readlines():
    y = linha.replace(original, alterada)
    f2.write(y)
f1.close()
f2.close()

os.remove(nome1)
os.rename(nome2,nome1)
