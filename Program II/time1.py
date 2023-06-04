import time

nome = input('Qual seu nome?')
f = open('registro.txt', 'a')
f.write(time.ctime()+'/' + nome + '\n')
f.close()
