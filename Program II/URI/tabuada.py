N = int(input())

if not(2<N<1000):
    N = int(input())

a = 1
while a <=10:
    result = a*N
    print(a, 'x', N, '=', result)
    a += 1
