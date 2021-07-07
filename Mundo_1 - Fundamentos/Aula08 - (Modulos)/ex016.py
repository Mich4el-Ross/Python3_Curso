"""
Desafio 016

Problema:   Crie um programa que leia um número Real qualquer pelo teclado
            e mostre na tela a sua porção Inteira.

            Ex: Digite um número: 6.127
                O número 6.127 tem a parte Inteira 6.
"""

from math import floor
num = float(input('Digite um numero real:'))
print('O numero {} tem a parte inteira {}'.format(num, floor(num)))
print('-'*30)