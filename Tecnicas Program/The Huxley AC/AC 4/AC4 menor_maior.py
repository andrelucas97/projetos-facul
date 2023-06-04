def le_e_devolve_menor():
    n = int(input())
    a = n
    while n >= 0:
        if n < a:
            a = n
        n = int(input())
    if (a < 0):
        a = 0
    return a

def le_e_devolve_maior():
    n = int(input())
    a = n
    while n >= 0:
        if n > a:
            a = n
        n = int(input())
    if (a < 0):
        a = 0
    return a

opcao = input()
if opcao == 'menor':
	menor = le_e_devolve_menor()
	print(menor)
elif opcao == 'maior':
	maior = le_e_devolve_maior()
	print(maior)
