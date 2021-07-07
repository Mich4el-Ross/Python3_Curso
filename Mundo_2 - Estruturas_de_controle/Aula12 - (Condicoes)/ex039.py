"""
Desafio 039

Problema: Faça um programa que leia o ano de nascimento de um jovem e
          informe, de acordo com sua idade:
          - Se ele ainda vai se alistar
          - Se é a hora de ele se alistar
          - Se já passou do tempo de alistamento

         O programa deve mostrar o tempo restante ou o que passou
"""

from datetime import date

year = date.today().year
birth = int(input('Informe o ano de seu nascimento: '))
age = year - birth
print('')

print('-=-'*18)

if age < 18:
    print('Voce ainda ira se ALISTAR.')
    print('Faltam {} anos para voce fazer seu alistamento'.format(18 - age))
    print('Seu alistamento será no ano de {}'.format(year + (18 - age)))
elif age == 18:
    print('Esta na hora de você se ALISTAR')
else:
    print('Já passou da hora de você se ALISTAR')
    print('Você deveria ter se alistado há {} anos, no ano de {}'.format(age - 18, year - (age - 18)))

print('-=-'*18)