arquivo = open('compras.txt', 'w')
item = input('Informe o que deseja escrever no arquivo: ')
arquivo.write(item)
arquivo.close()
