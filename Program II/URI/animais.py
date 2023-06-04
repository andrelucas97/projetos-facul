a = input()
b = input()
c = input()

if a == 'vertebrado':
    if b == 'ave':
        if c == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if c == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if b == 'inseto':
        if c == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if c == 'onivoro':
            print('minhoca')
        else:
            print('sanguessuga')
