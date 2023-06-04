N = 0
if N == 0:
    while (N <= 5) or (N >= 2000):
        N = int(input())
a = 2
while a <= N:
    result = a**2
    print('%d^2' % a, '=', result)
    a += 2


