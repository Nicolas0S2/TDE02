vetor = [0] * 15
no_rep = []
for c in range(15):
    vetor[c] = int(input(f'Digite o {c + 1}º número: '))
null = vetor.count(0)
for i in range(null):
    vetor.remove(0)
for d in range(null):
    vetor += [0]
print(vetor)
