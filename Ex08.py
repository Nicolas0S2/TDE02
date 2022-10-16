vetor_1 = [0] * 10
vetor_2 = [0] * 10
vetor_3 = [0] * 20
cont = 0
for c in range(len(vetor_1)):
    vetor_1[c] = int(input(f'Digite o {c + 1}º valor: '))
print('\n')
for i in range(len(vetor_2)):
    vetor_2[i] = int(input(f'Digite o {i + 1}º valor: '))
for d in range(0, len(vetor_3), 2):
    if cont <= 9:
        vetor_3[d] = vetor_1[cont]
        cont += 1
cont = 0
for e in range(1, len(vetor_3), 2):
    if cont <= 9:
        vetor_3[e] = vetor_2[cont]
        cont += 1
print('\nO vetor 03 é: ')
print(vetor_3)
