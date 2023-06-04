sb = float(input("Salário bruto: "))
tempo = int(input("Tempo: "))
emp = float(input("Valor emprestado: "))

if sb > 2000.00:
    if tempo > 2:
        juros = emp * 0.15
    else:
        juros = emp * 0.20
    print(emp + juros)
else:
    print('Empréstimo negado')
