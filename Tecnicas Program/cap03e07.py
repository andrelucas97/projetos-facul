qtdRestante = float(input("Informe o valor do produto: R$"))

qtdCedulas = qtdRestante // 100
qtdRestante = qtdRestante - (qtdCedulas * 100)
print("Qtd de cédulas de R$100:", qtdCedulas)
print("Qtd restante em R$:", qtdRestante)

qtdCedulas = qtdRestante // 50
qtdRestante = qtdRestante - (qtdCedulas * 50)
print("Qtd de cédulas de R$50:", qtdCedulas)
print("Qtd restante em R$:", qtdRestante)

qtdCedulas = qtdRestante // 20
qtdRestante = qtdRestante - (qtdCedulas * 20)
print("Qtd de cédulas de R$20:", qtdCedulas)
print("Qtd restante em R$:", qtdRestante)

qtdCedulas = qtdRestante // 10
qtdRestante = qtdRestante - (qtdCedulas * 10)
print("Qtd de cédulas de R$10:", qtdCedulas)
print("Qtd restante em R$:", qtdRestante)

qtdCedulas = qtdRestante // 5
qtdRestante = qtdRestante - (qtdCedulas * 5)
print("Qtd de cédulas de R$5:", qtdCedulas)
print("Qtd restante em R$:", qtdRestante)

qtdCedulas = qtdRestante // 2
qtdRestante = qtdRestante - (qtdCedulas * 2)
print("Qtd de cédulas de R$2:", qtdCedulas)
print("Qtd restante em R$:", qtdRestante)

qtdCedulas = qtdRestante // 1
qtdRestante = qtdRestante - (qtdCedulas * 1)
print("Qtd de cédulas de R$1:", qtdCedulas)
print("Qtd restante em R$:", qtdRestante)
