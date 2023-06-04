N = 10001

if N == 10001:
    while N >= 10000:
        N = int(input('N: '))

a = 0

par = 'EVEN'
impar = 'ODD'
pos = 'POSITIVE'
neg = 'NEGATIVE'

m1 = ''
m2 = ''

while a < N:
    X = int(input())
    if X%2 == 0:
        if X == 0:
            print('NULL')
        else:
            m1 = par
    else:
        m1 = impar

    if X != 0:
        if X > 0:
            m2 = pos
        else:
            m2 = neg
        print(m1, m2)
    a += 1
