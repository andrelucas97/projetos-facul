def todos_os_indices(seq, x):
    n = len(seq)
    result = []
    a = 0
    for i in range(n):
        if seq[i] == x:
            result.append(a)
            result[a] = i
            a += 1
    return result
    











sequencia = eval(input())
valor = eval(input())
resultado = todos_os_indices(sequencia, valor)
if isinstance(resultado, list):
	if len(resultado) > 0:
		for item in resultado:
			print(item)
	else:
		print('lista vazia')
else:
	print('Erro. Voce deve devolver uma lista')
