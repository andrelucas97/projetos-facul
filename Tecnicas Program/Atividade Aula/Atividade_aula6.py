def tabuada(n, modo):
    cont1 = 1
    adicao = 0
    multi = 1
    cont2 = 1
    
    if modo == 1:
        while cont1 <= 10:
            adicao = adicao + n
            cont1 += 1
        return adicao
    else:
        while cont2 <= 10:
            multi = multi * n
            cont2 += 1
        return multi
