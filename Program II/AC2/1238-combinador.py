N = int(input())

for i in range(N):
    x = input().split()

    p1 = x[0]
    p2 = x[1]
    tam1 = len(p1)
    tam2 = len(p2)
    
    result = ""
    j = 0
    while (j < tam1 and j < tam2):
        result += p1[j] + p2[j]        
        j += 1
    if j < tam1:
        result+= p1[j:]

    if j < tam2:
        result += p2[j:]
    

    print(result)
