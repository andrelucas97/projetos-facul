lista = ['roteador', 'switch', 'modem', 'servidor', 'firewall']
lista.append('transceiver')
del lista[2]
lista.insert(0, 'gbic')
print(lista[0])
print(lista[2])
print(lista[5])
