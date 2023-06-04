valido = False
while not valido:
    per = float(input('Digite o valor percentual (0 a 1 ou 10 a 100: '))
    preco = float(input('Digite o preço: '))
    if (0 <= per <= 1) or (10 <= per <= 100):
        valido = True
    else:
        print('Fora da faixa! Digite novamente.')

if (0 <= per <= 1):
    novo_preco = preco * per
    print(novo_preco)
else:
    novo_preco = preco * per/100
    print(novo_preco)
