from random import randint


vetor = [0] * 50
for c in range(len(vetor)):
    vetor[c] = randint(0, 20)
print(vetor)
print('A soma é de: ', sum(vetor))
print(f'O número 9 apareceu {vetor.count(9)} vezes.')
print(f'O maior valor é {max(vetor)}')
print(f'O menor valor é: {min(vetor)}')
