N = 10001

if N >= 10000:
    while N >= 10000:
        N = int(input())


a = 1
while a <= 10000:
    if a%N == 2:
        print(a)
    a += 1
