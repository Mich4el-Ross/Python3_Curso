"""
Desafio 060

Problema: Faça um programa que leia um número qualquer e mostre o seu
          fatorial
"""

from time import sleep

num = int(input('Digite um número: '))
cont = num
fact = 1

print('\033[1;32mCalculando {}!...\033[m'.format(num))
sleep(2)
print('')

while cont > 0:

    print('{}'.format(cont), end='')
    print(' X ' if cont > 1 else ' = ', end='')

    fact *= cont
    cont -= 1

print('{}'.format(fact))