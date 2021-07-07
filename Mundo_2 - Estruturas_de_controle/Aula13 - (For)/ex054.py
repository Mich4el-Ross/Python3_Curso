"""
Desafio 054

Problema: Crie um programa que leia a data de nascimento de sete pessoas. No
          final mostre quantas pessoas já atingiram a maioridade e quantas
          ainda não
"""

from datetime import date

year = date.today().year
older = 0
under = 0

for x in range(1, 8):
    date = int(input('{} ° pessoas - Data de nascimento: '.format(x)))
    age = year - date
    if age >= 18:
        older += 1
    else:
        under += 1

print('')
print('Foram cadastradas {} maiores de idade'.format(older))
print('Foram cadastradas {} menores de idade'.format(under))