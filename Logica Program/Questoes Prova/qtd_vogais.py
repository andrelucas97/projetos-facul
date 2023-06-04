def qtd_vogais(v, n):
    
    qtd = 0
    i = 0
    while i < n:
        if v[i] == 'a' or v[i] == 'e' or v[i] == 'i' or v[i] ==  'o' or v[i] ==  'u' :
            print(v[i])
            qtd += 1
        i += 1
    return qtd

v = ['a', 'b', 'c', 'd', 'e', 'f', 'u', 'i', 'j']
n = len(v)
print(qtd_vogais(v, n))
