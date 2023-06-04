salario = float(input())

if (0 <= salario <= 400):
    percentual = 15
    reajuste = salario * 0.15
    novoSalario = salario + reajuste
else:
    if (400.01 <= salario <= 800):
        percentual = 12
        reajuste = salario * 0.12
        novoSalario = salario + reajuste
    else:
        if (800.01 <= salario <= 1200):
            percentual = 10
            reajuste = salario * 0.10
            novoSalario = salario + reajuste
        else:
            if (1200.01 <= salario <= 2000.00):
                percentual = 7
                reajuste = salario * 0.07
                novoSalario = salario + reajuste
            else:
                percentual = 4
                reajuste = salario * 0.04
                novoSalario = salario + reajuste

print('Novo salario:', "%.2f" % novoSalario)
print('Reajuste ganho:', "%.2f" % reajuste)
print('Em percentual:', percentual, '%')
