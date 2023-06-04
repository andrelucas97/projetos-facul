X = float(input())

N = []

N.append(X)

for i in range (1, 100):
    N.append((N[i-1]/2))

for j in range(100):
    print('N[%i] = %.4f' % (j, N[j]))
