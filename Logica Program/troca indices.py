'''
v = [10, 20, 30, 40, 50]
chamar função troca(v, i, j) e trocar os indices i e j
exemplo: i=1 e j=4 -- troca(v, i, j)
o novo v = [10, 50, 30, 40, 20]
'''

def exibe(v, n):
    for i in range(n):
        print(v[i], end= ' ')

def troca (v, i, j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp
'''    
def troca(v, i, j):
    (v[i], v[j]) = (v[j], v[i])

    = (v[i], v[j] = ((50), (20))
     20->50  50->20     
'''


v = [10, 20, 30, 40, 50]
troca(v, 1, 4)
exibe(v, 5)
