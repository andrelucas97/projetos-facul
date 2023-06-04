#Questao 2

dividendo = int(input("Dividendo: ")) #30
divisor = int(input("Divisor: ")) #5
x = 1

while dividendo >= divisor:
    quociente = x
    resto = dividendo - divisor
    x = x + 1
    dividendo = dividendo - divisor

print("O resto é: ", resto)
print("O quociente é: ", quociente)
    
