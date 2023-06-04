'''
para todo i em [0 a 'n-1'[ é verdade que v[i] <= v[i+1]

      0   1   2   3   4
v = [10, 20, 30, 40, 50]

'''
import random
random.seed()

def aleatorio(i, f): #i=inicio/ f=final
    return random.randint(i, f)
    

def crescente(v, n):
    for i in range(n-1):
        if v[i] > v[i+1]: #Se isso 'v[i] <= v[i+1]' for falso..
            return False
    return True

def decrescente(v, n):
    for i in range(n-1):
        if v[i] < v[i+1]: #Se isso 'v[i] >= v[i+1]' for falso..
            return False
    return True



def troca(v, i, j):
    v[i], v[j] = v[j], v[i]
    
#----------------------------------------------

def empurra(v, n): #colcoar na ordem crescente
    for i in range(n-1): # [0...n-1[
        if v[i] > v[i+1]:
            troca(v, i, i+1)

def bubble_sort(v, n):
    for i in range(n, 1, -1):
        empurrra(v, i)
