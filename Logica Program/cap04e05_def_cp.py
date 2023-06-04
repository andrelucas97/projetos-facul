# com parametro

def valor_venda(prod):
    if prod < 20.0:
        venda = prod * 1.45
    else:
        venda = prod * 1.30
    print('O valor da venda será: R$ %.2f' % venda)
    return

p = float(input('Produto: '))
valor_venda(p)
