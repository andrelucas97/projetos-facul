from time import sleep

h = 0
while h < 24:
    m = 0
    while m < 60:
        s = 0
        while s < 60:
            print('%.2d:%.2d:%.2d' % (h, m, s))
            sleep(1)
            s += 1
        m += 1
    h += 1
    
"""
for h in range(24):
    for m in range(60):
        for s in range(0, 60, 1): #ou 'for s in range(60):'
            print('%02d:%02d:%02d' % (h, m, s))
            sleep(1)
"""

