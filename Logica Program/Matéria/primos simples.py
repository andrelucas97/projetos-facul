def primo(n):
    if n == 1:
        return False

    divisor = 2

    while n % divisor != 0:
        divisor += 1
    return divisor == n #se divisor for == n, retorna True

