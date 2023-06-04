def qtd_divisores(n):
    qtd = 0
    for divisor in range (1, n+1):
        if n % divisor == 0:
            qtd += 1
    return qtd

#------------------------------------

def primo(n):
    return qtd_divisores(n) == 2

#-------------------------------------

def intervalo_primo(a, b):
    for num in range(a, b+1):
        if primo(num):
            print(num)
