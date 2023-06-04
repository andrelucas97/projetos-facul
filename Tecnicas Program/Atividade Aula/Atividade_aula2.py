def exibe_status(n_aluno, f_aluno):
    if n_aluno >=5.0 and f_aluno <= 25:
        if n_aluno >= 7.0 and f_aluno <= 25:
            print("Aluno aprovado!")
        else:
            print("Aluno em recuperação!")
    else:
        print("Aluno reprovado!")
    return
n_aluno = float(input("Insira a nota: "))
f_aluno = int(input("Insira as faltas: "))

"""
    if n_aluno < 5.0 or f_aluno < 25:
        print("Aluno Reprovado")
    else:
        if n_aluno >= 7.0 and f_aluno >=25:
            print("Aluno aprovado!")
        else:
            print("Aluno em recuperação!")
"""

