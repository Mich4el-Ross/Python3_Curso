"""
Desafio 071

Problema: Crie um programa que simule o funcionamento de um caixa eletrônico.
          No início, pergunte ao usuário qual será o valor a ser sacado e o
          programa vai informar quantas cédulas de cada valor serão entregues.

          OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

from time import sleep
tot50 = tot20 = tot10 = tot1 = 0

print('-=-' * 15)
print('{:^45}'.format('CAIXA ELETRÔNICO MD'))
print('-=-' * 15 + '\n')

value = int(input('Informe a quantia do saque: R$ '))

while True:

    if value >= 50:
        value -= 50
        tot50 += + 1
    elif value >= 20:
        value -= 20
        tot20 += 1
    elif value >= 10:
        value -= 10
        tot10 += 1
    else:
        value -= 1
        tot1 += 1

    if value == 0:
        break

print('\033[1;32mAnalisando...\033[m')
sleep(2)

print('\n' + '-=-' * 15)
print('{:^45}'.format('Seu saque tera um'))
print('Total de {} cédulas de R$50'.format(tot50))
print('Total de {} cédulas de R$20'.format(tot20))
print('Total de {} cédulas de R$10'.format(tot10))
print('Total de {} cédulas de R$1'.format(tot1))
print('-=-' * 15)