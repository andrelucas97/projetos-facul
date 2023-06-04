def qtd_divisores(n):
    qtd = 0
    for divisor in range (1, n+1): #[1..n+1[
        if n % divisor == 0:
            qtd += 1
    return qtd

def primo(n):
    return qtd_divisores(n) == 2 # (return True ou return False)

    # if qtd_divisores(n) == 2:
      #  return True -- encerra a função
     #return False

n = int(input('n: '))

if primo(n):
    print('É primo!')
else:
    print('Não é primo!')
        
