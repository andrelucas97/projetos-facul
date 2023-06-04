def eh_primo(n):
    while n <= 0:
        n = int(input("Digite novamente: "))

    cont1 = 1
    x = 0
    qtd = 0
    while n >= cont1:
        resto = n % cont1
        if resto == 0:
            qtd += 1
        cont1 += 1
        
    if qtd <= 2:
        print("É primo!")
    else:
        print("Não é primo")
    return eh_primo

"""
for divisor in range(1, n+1):
        resto = n % divisor
        if resto == 0:
            qtd += 1
    if qtd <= 2:
        print("É primo!")
    else:
        print("Não é primo")
"""
