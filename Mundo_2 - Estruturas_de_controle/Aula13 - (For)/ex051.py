"""
Desafio 051

Problema: Desenvolva um programa que leia o primeiro termo e a razão de uma
          PA e no final mostre os 10 primeiros termos dessa progressão
"""

a1 = int(input('Digite o primeiro termo dessa PA: '))
r = int(input('Digite a razão dessa PA: '))
n_term = a1 + (10-1) * r

print('\nCom primeiro termo = {} e razão = {}'.format(a1, r))
print('A nossa PA de 10 termos fica:')

for x in range(a1, n_term, r):
    print(x, end=' ➙ ')
print('FIM')