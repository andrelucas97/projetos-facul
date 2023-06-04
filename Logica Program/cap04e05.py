precoProduto = float(input('Insira o preço do produto: R$'))

if precoProduto < 20.0:
    venda = precoProduto * 1.45
    print('O valor da venda é:', venda)
else:
    venda = precoProduto * 1.30
    print('O valor da venda é:', venda)

