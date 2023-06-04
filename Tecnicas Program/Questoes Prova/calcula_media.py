def calcula_media(n1, n2, n3):
    resultado = (n1 + n2 + n3)/3
    return resultado

a = float(input('Nota 1: '))
b = float(input('Nota 2: '))
c = float(input('Nota 3: '))
media = calcula_media(a, b, c)
print(media)
