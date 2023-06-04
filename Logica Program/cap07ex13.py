def menor (v, n):
    m = 0
    for i in range (1, n):
        if v[i] < v[m]:
            m = i
    return m

def preenche(v, n):
    for i in range(n):
        v[i] = int(input('v[%d]:' % i))
    return

n = 10
v = n * [0]
preenche(v, n)
print('Indice do Menor:', menor(v, n))

