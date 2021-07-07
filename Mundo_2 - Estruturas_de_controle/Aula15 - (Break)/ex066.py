"""
Desafio 064

Problema: Crie um programa que leia vários números inteiros pelo teclado.
          O programa só vai parar quando o usuário digitar o valor 999. No
          final, mostre quantos números foram digitados e qual foi a soma
          entre eles.
"""

from time import sleep
cont = add = 0

while True:
    num = int(input('Insira um número [999 para PARAR]: '))

    if num == 999:
        print('\n\033[1;31mFinalizando...\033[m')
        sleep(2)
        break

    cont += 1
    add += num

print('\n' + '-=-'*16)
print('Você inseriu {} numeros e a soma entre eles é {}'.format(cont, add))
print('-=-'*16)