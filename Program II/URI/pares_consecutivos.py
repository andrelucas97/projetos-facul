X = int(input())
a = 0
imp = 0
if X%2 == 0:
    imp = X + 1
    print(imp)
    a = 1
    while a < 6:
        imp += 2
        a += 1
        print(imp)
else:
    imp = X
    print(imp)
    while a < 5:
        imp += 2
        print(imp)
        a += 1
