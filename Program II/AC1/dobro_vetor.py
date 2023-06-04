'''
N = []
i = 0
V = int(input())
while i <= 10:    
    N.append(V)
    X = N[i]
    print('N[%d] = %d' % (i, X))
    V *= 2
    i += 1
'''

N = []
V = int(input())

for i in range (10):
    N.append(V)
    V = V * 2

for j in range (10):
    print('N[%i] = %i' % (j, N[j]))
