# sem parametro

def valor_venda():
    prod = float(input('Produto: '))
    if prod < 20.0:
        venda = prod * 1.45
    else:
        venda = prod * 1.30
    print('O valor da venda será: R$ %.2f' % venda)
    return

valor_venda()
