media_provas = float(input())
media_trabalhos = float(input())
qtd_faltas = int(input())

if media_provas >= 6 and media_trabalhos >= 5 and qtd_faltas < 8:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')
