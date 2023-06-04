a = 1
result = 0
while a <= 5:
    valor = float(input())
    if valor%2 == 0:
        result += 1
    a += 1

print(result, 'valores pares')
