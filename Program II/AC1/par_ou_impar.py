impar = []
i = 0
par = []
p = 0
for p1 in range (15):
    valor = int(input())
    if valor%2 == 0:
        par.append(valor)
        p += 1
    else:
        impar.append(valor)
        i += 1
        
    if p > 4:        
        for p2 in range (0, 5):
            print('par[%i] = %i' % (p2, par[p2]))
        par = []
        p = 0
    
    if i > 4:        
        for i1 in range (5):
            print('impar[%i] = %i' % (i1, impar[i1]))
        impar = []
        i = 0
for i2 in range (len(impar)):
    print('impar[%i] = %i' % (i2, impar[i2]))

for p3 in range (len(par)):
    print('par[%i] = %i' % (p3, par[p3]))
