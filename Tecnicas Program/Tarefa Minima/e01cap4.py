def salario():
    s1 = float(input('Insira seu Salario: '))
    s2 = float(input('Insira seu Salario: '))
    if s1 >= s2:
        maior = s1
    else:
        maior = s2

    salarioFinal = maior * 1.2
    print('R$', "%.2f" % salarioFinal)
