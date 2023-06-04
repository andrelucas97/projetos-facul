N = []
T = int(input())

rep = 1000//T

for i in range (rep+1):
    a = 0    
    while T > a:
       N.append(a)
       a += 1
for j in range (1000):
    print('N[%i] = %i' % (j, N[j]))
