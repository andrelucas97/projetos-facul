a = float(input())
b = float(input())
c = float(input())

if (a<b+c and b<a+c and c<a+b):
    if (a==b and b==c):
        print(equilátero)
    else:
        if (a==b or a==c or b==c):
            print('isósceles')
        else:
            print('escaleno')
else:
    print('Invalido')
        
        
