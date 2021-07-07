"""
Desafio 074

Problema: Crie um programa que vai gerar 5 números aleatórios e colocar em
          uma tupla. Depois disso, mostre a listagem de números gerados e
          também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

print('-=-' * 10)
print(f'{"SORTEIO" :^30}')
print('-=-' * 10)

numbers = ()
for x in range(1, 6):
    numbers += randint(1, 10),

print('Numeros sorteados: ', end=' ')
for y in numbers:
    print(f'{y}', end=' ')

print(f'\nMaior número: {max(numbers)}')
print(f'Menor número: {min(numbers)}')