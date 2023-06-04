N = int(input())
a = {}
b = []
for i in range(N):
    x = int(input())
    if not (x in a):
        b.append(x)
    if not (x in a):
        a[x] = 1
    else:
        a[x] += 1

b.sort()

for j in range(len(b)):
    print('%i aparece %i vez(es)' % (b[j], a[b[j]]))


'''
N = int(input())
a = []


for i in range(N):
    x = float(input())
    a.append(x)
    
a.sort()
tam = len(a)

for j in range(tam):
    rep = 0
    for z in range(tam):
        if a[j] == a[z]:
            rep += 1
    if a[j]!= a[j-1]:
        print('%i aparece %i vez(es)' % (a[j], rep))
''' 
  

