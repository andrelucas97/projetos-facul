

while True:
    x = input().split()
    if (x[0] == '0' and x[1] == '0'):
        break
    else:       
        qtdDigitos = int(x[0])
        qtdApagados = int(x[1])

        numb = input()
        cont1 = 0
        pos_menor = 0    

        comp = 10
        while qtdApagados > 0:
            while cont1 < qtdDigitos:
                if int(numb[cont1]) < comp:
                    pos_menor = cont1
                    comp = int(numb[cont1])
                cont1 += 1
            numb = numb[0:pos_menor] + numb[pos_menor+1:]

            
            
            comp = 10
            cont1 = 0
            qtdApagados -=1
            qtdDigitos -= 1
    print(numb)
