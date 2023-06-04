n = int(input())
comp = n

while n >= 0:
    if n > comp:
        comp = n
    n = int(input())    

print(comp)
