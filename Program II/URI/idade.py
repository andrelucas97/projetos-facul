idade = int(input())

ano = idade//365
mes = (idade%365)//30
dia = (idade%365)%30

print(ano, "ano(s)")
print(mes, "mes(es)")
print(dia, "dia(s)")
