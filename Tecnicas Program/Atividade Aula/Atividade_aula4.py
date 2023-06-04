n = float(input())
num = 1
soma = 0

for num in range(1, n-1+1, 1):
    denominador = n
    soma = soma + (num/denominador)
    n = n-1

print(soma)
