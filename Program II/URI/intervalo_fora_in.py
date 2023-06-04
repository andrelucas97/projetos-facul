N = int(input())

if N >= 10000:
    while N >= 10000:
        N = int(input())
a = 0
dentro = 0
fora = 0
while a < N:
    X = int(input())
    if (10 <= X <= 20):
        dentro += 1
    else:
        fora += 1
    a += 1
print(dentro, "in")
print(fora, "out")
    
