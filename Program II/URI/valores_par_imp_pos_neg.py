a = 1
resultPar = 0
resultImpar = 0
resultPos = 0
resultNeg = 0
while a <= 5:
    valor = float(input())
    if valor%2 == 0:
        if valor > 0:
            resultPos += 1
        else:
            if valor < 0:
                resultNeg += 1
            
        resultPar += 1
        
    if valor%2 != 0:
        if valor > 0:
            resultPos += 1
        else:
            if valor < 0:
                resultNeg += 1
            
        resultImpar += 1
    a += 1

print(resultPar, 'valor(es) par(es)')
print(resultImpar, 'valor(es) impar(es)')
print(resultPos, 'valor(es) positivo(s)')
print(resultNeg, 'valor(es) negativo(s)')
