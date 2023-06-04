
def checa_quantidade_divisores(n, qtd):
    i = 1
    divisores = 0
    while n >= i:        
        resto = n % i
        if resto == 0:
            divisores += 1
        i += 1
    print(divisores)
    print(qtd)
    
    if (qtd != divisores):
        return False
    else:
        return True
    

n = int(input())
qtd = int(input())
if checa_quantidade_divisores(n, qtd):
    print(n, "possui", qtd, "divisores")
else:
    print(n, "nao possui", qtd, "divisores")

	
"""
qtd = int(input())
n = int(input())

i = 1
divisores = 0
while qtd >= i:        
    resto = n % i
    if resto == 0:
        divisores += 1
    i += 1
print(divisores)
"""
