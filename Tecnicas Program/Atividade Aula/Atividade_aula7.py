lst = ['cereal', 'banana', 'maçã', 'melão', 'iogurte']
lista = len(lst)

def imprime_lista(lista):
    a = 0
    while a < lista:
        print(a, "-", lst[a])
        a = a + 1
    return lst

imprime_lista(lista)

print("Tamanho da lista: ", lista)

lst.append(input("Novo elemento: "))

print("Nova lista: ", lst)

del lst[2]

print("Nova lista: ", lst)

