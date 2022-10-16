vetor = [0] * 20
no_rep = []
for c in range(20):
    vetor[c] = int(input(f'Digite o {c + 1}º número: '))
print('\nSem valores repetidos: ')
for item in vetor:
    if item not in no_rep:
        no_rep += [0]
        no_rep[-1] = item
print(no_rep)
