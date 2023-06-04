salario_bruto = float(input())
tempo_relacionamento = int(input())
valor_emprestimo = float(input())
if salario_bruto > 2350:
    if tempo_relacionamento >= 5:
        juros = valor_emprestimo * 0.10
    elif 2 <= tempo_relacionamento < 5:
        juros = valor_emprestimo * 0.15
    else:
        juros = valor_emprestimo * 0.2
    print('O valor dos juros é: ', juros)

else:
    print('Empréstimo negado')
