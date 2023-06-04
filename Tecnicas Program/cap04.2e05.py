def funcao_fx(x):
    if x <= 1:
        fx = 1
    elif(x > 1) and (x <= 2):
        fx = 2
    elif(x > 2) and (x <= 3):
        fx = x**2
    else:
        fx = x**3
    print(fx)
    return
    
x = float(input('x = '))
funcao_fx(x)

