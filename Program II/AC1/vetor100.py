A = []

for i in range (4):
    valor = float(input())
    A.append(valor)
for j in range (4):
    if A[j] <= 10:
        print('A[%i] = %.1f' % (j, A[j]))
