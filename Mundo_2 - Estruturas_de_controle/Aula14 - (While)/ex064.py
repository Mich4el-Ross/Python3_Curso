"""
Desafio 063

Problema: Crie um programa que leia vários números inteiros pelo teclado.
          O programa só vai parar quando o usuário digitar o valor 999. No
          final, mostre quantos números foram digitados e qual foi a soma
          entre eles.
"""

from time import sleep
number = add = cont = 0

while number != 999:
    number = int(input('Digite um número [999 para parar]: '))

    if number != 999:
        add += number
        cont += 1
    else:
        print('\n\033[1;31mFinalizando...\033[m')
        sleep(2)

print('\n' + '-=-'*16)
print('Você inseriu {} numeros e a soma entre eles é {}'.format(cont, add))
print('-=-'*16)