valores = [0] * 6
for c in range(6):
    num = int(input(f'Digite o {c + 1}º valor: '))
    valores[c] = num
valores.reverse()
print('\n')
print('Valores: ', valores)
