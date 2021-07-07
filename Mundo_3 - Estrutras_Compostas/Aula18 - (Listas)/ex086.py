"""
Desafio 086

Problema: Crie um programa que crie uma matriz 3x3 e preencha com valores lidos
          pelo teclado. Mostre-a no final.
"""

matriz = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
]

for r in range(0, 3):
    for c in range(0, 3):
        matriz[r][c] = int(input(f'Insira um valor para [{r}, {c}]: '))

print('\n' + '-=-' * 15)
print(f'{"A MATRIZ INSERIDA FOI":^45}')
print('-=-' * 15 + '\n')

for r in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[r][c]:^5}]', end=' ')
    else:
        print()