"""
Desafio 078

Problema:  Faça um programa que leia 5 valores numéricos e guarde-os em uma
           lista. No final mostre o maior e o menor valor e suas respectivas
           posições
"""

values = []

for x in range(0, 5):
    values.append(int(input(f'Digite o {x+1}° valor: ')))

print('\n' + '-=-' * 20)
print(f'Você digitou os seguintes valores: {values}')

print(f'O MAIOR valor digitado é {max(values)} e se encontra nas posições ', end='')
for p, v in enumerate(values):
    if v == max(values):
        print(f'{p+1}...', end=' ')

print(f'\nO MENOR valor digitado é {min(values)} e se encontra nas posições ', end='')
for p, v in enumerate(values):
    if v == min(values):
        print(f'{p+1}...', end=' ')
print('\n' + '-=-' * 20)