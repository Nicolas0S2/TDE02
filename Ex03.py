vetor = []
num = 0
cont = 0
soma_par = 0
soma_impar = 0
while num >= 0:
    num = int(input('Digite um inteiro: '))
    if num >= 0:
        vetor += [0]
        vetor[-1] = num
    else:
        break
for item in range(len(vetor)):
    if vetor[item] > 5:
        cont += 1
    if vetor[item] % 2 == 0:
        soma_par += vetor[item]
    else:
        soma_impar += vetor[item]
print('\n')
print(f'O número de valores maior que 5 é de: {cont}')
print(f'A soma de valores pares armazenados no vetor é de: {soma_par}')
print(f'A soma de valores impares armazenados no vetor é de: {soma_impar}')
print(f'A quantidade total de valores armazenados é de: {len(vetor)}')
