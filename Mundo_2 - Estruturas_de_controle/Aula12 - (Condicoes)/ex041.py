"""
Desafio 041

Problema: A Confederação Nacional de Natação precisa de um programa
          que leia o ano de nascimento de um atleta e mostre sua
          categoria, de acordo com a idade:
          - Até 9 anos: MIRIM
          - Até 14 anos: INFANTIL
          - Até 19 anos: JÚNIOR
          - Até 25 anos: SÊNIOR
          - Acima de 25 anos: MASTER
"""

from datetime import date

year = date.today().year
born = int(input('Ano de nascimento: '))
age = year - born

print('\nVocê tem {} anos'.format(age))

if age <= 9:
    print('Classificação: MIRIM')
elif age <= 14:
    print('Classificação: INFANTIL')
elif age <= 19:
    print('Classificação: JUNIOR')
elif age <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')