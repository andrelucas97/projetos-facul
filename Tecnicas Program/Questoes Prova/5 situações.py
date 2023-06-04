distancia = float(input())

if distancia < 10:
    print('Muito próximo')
elif distancia <= 12:
    print('Próximo')
elif distancia <=26:
    print('Distancia moderada')
elif distancia <= 50:
    print('Longe')
else:
    print('Muito longe')
