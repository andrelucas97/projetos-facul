import time


Fib = []
Fib.append(0)
Fib.append(1)
N = int(input())
t1 = time.time()
for i in range (2, N+1):        
        Fib.append(Fib[i-2]+Fib[i-1])        
      
t1 = time.time()
print('Fib(%i) = %i' % (N, Fib[N]))
t2 = time.time()

print(t2-t1, 'segundos')
'''
T = int(input())

Fib = []
Fib.append(0)
Fib.append(1)
for i in range (2, 60):        
        Fib.append(Fib[i-2]+Fib[i-1])        
for j in range (T):        
    N = int(input())    
    print('Fib(%i) = %i' % (N, Fib[N]))



#simples porem mt lento

def fib(n):
        if n == 0:
                return 0
        elif n == 1:
                return 1
        else:
                return (fib(n-1) + fib(n-2))
'''
