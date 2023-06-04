total = 0
qtd = 0
preco = float(input())

while preco >= 0:
    total += preco
    qtd += 1
    preco = float(input())

if total > 200.00 and qtd > 10:
    total *= 0.95

print('%2f' % total)
