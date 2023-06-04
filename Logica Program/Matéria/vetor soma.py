def somar(v, n):
    soma = 0
    for i in range (n):
        soma = soma+v[i]
    return soma

peso = [10, 20, 30]
X = somar(peso, 3)
print("A soma é:", X)
