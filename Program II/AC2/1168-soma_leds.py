num = {
    '1':2,
    '2':5,
    '3':5,
    '4':4,
    '5':5,
    '6':6,
    '7':3,
    '8':7,
    '9':6,
    '0':6}

n = int(input())

for i in range (n):
    soma = 0
    x = input()
    
    for j in range(len(x)):
        soma += num[x[j]]
    print(soma, 'leds')




















        
