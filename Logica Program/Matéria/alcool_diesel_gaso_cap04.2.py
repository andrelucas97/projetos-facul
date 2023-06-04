qtd = float(input('quantidade: '))
tipo = input('Tipo: ')

if tipo == 'a':
    total = qtd * 3.8997
else:
    if tipo == 'd':
        total = qtd * 3.6543
    else:
        total = qtd * 4.4009
print(total)
        
