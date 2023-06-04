def menor (v, n):
    m = v[0]
    for i in range (1, n):
        if v[i] < m:
            m = v[i]
    return m

def preenche(v. n):
    for i in range(n):
        v[i] = int(input('v[%d]:' % i))
    return

n = 10
v = n * [0]
preenche(v, n)
print('Menor:', menor(v, n))
