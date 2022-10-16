vetor = [0] * 10
no_rep = []
for c in range(10):
    vetor[c] = int(input(f'Digite o {c + 1}º número: '))
print('\nOs valores repetidos foram: ')
for item in range(len(vetor)):
    if vetor[item] not in no_rep:
        if vetor.count(vetor[item]) >= 2:
            print(vetor[item])
            no_rep += [0]
            no_rep[-1] = vetor[item]
