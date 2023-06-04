N = int(input())
par = []
impar = []
for x in range(N):    
    number = int(input())
    if number % 2 == 0:
        par.append(number)
    else:
        impar.append(number)

        
par.sort()
impar.sort(reverse=True)

for p in par:
    print(p)

for i in impar:
    print(i)
