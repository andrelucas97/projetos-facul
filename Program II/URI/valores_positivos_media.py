a = 1
result = 0
soma = 0
while a <= 6:
    valor = float(input())
    if valor > 0:
        result += 1
        soma = soma + valor
    a += 1
    
print(result, 'valores positivos')
print(round(soma/result, 1))
