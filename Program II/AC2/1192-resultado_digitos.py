N = int(input())
a = []

for i in range (N):
    x = input()
    a = x[0]
    b = x[1]
    c = x[2]
    
    if a == c:
        result = int(a)*int(c)
        print(result)
        
    elif b.upper() == b:
        result = int(c) - int(a)
        print(result)
        
    else:
        result = int(a) + int(c)
        print(result)
