X = []
a = 0
while a < 10:
    valor = int(input())
    X.append(int(valor))
    if X[a] <= 0:
        X[a] = 1
    print('X[%d] = %d' % (a, X[a]))
    a += 1
