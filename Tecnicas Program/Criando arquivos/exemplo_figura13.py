arquivo = open('compras.txt', 'r')
for linha in arquivo:
    linha = linha.rstrip() # para nao pular linha
    print(linha)
arquivo.close()
