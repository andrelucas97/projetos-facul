saida = True

while saida:
    i = 0
    x = input()
    
    if x != '*':
        a = []
        neg = 0
        xUp = x.upper()
        
        for i in xUp.split():
            a.append(str(i))
            
        for j in range(len(a)-1):
            if a[j][0] != a[j+1][0]:
                neg += 1
                
        if neg != 0:
            print('N')
        else:
            print('Y')    
                
    else:
        saida = False

