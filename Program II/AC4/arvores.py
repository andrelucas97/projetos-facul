N = int(input())
input()
vez = 0

for i in range(N):
    arvores = {}
    numArvores = 0
    arv = []

    while True:
        try:
            arvo = input()
            if arvo == '':
                break

            numArvores += 1
            if arvo in arvores:
                arvores[arvo] += 1
            else:
                arvores[arvo] = 1
                
        except EOFError:
            break

        
    for j in sorted(arvores):
        num = arvores[j]*(100/numArvores)
        print('%s %.4f' % (j, num))

    vez += 1
    if vez == N:
        break
    else:
        print()
