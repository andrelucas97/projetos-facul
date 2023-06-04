'''
Crie um programa que use uma funçao
que recebe como parametros um inteiro X,
um vetor de inteiros v, e o tamanho n de v.
A função deverá retornar verdadeiro se o item
x estiver em v, ou falso se o item x não estiver
em v.
'''

def busca(x, v, n):
    for i in range(n):
        if v[i] == x:
            return True    
    return False

# programa principal

v = [10, 20, 30, 40, 50]
n = 5 #len(v)
x = 20
