'''
n = int(input())
while n > 0:
    n -= 1
    c = input().split()
    c.sort(key=len, reverse=True)
    for i in range(len(c)):
        print(c[i], end = '')
        if i != len(c)-1:
            print(' ', end = '')
    print()

'''

n = int(input())
for i in range(n):
    a = []
    x = input()    
    for j in x.split():
        a.append(j)
            
    a.sort(key=len, reverse=True)
    
    for x in range(len(a)):
        print(a[x], end = '')
        if x != len(a)-1:
            print(' ', end = '')
    print()

