arquivo = open('compras.txt', 'a')
item = input('Nome do item: ')
while item != '':
    qtd = int(input('Quantidade: '))
    arquivo.write('item: %s | quantidade: %d\n' % (item, qtd))
    item = input('Nome do item: ')
arquivo.close()
