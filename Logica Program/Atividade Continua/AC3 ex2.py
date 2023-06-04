estudei = False

while not estudei:
    print('você é um universitário')
    print('só passará se estudar')
    caiu_a_ficha = input()
    if caiu_a_ficha == 'sim':
        estudei = True
    else:
        estudei = False
print('Ótimo! O esforço será recompensado')
