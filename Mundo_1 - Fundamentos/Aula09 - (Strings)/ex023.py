"""
Desafio 023

Problema:   Faça um programa que leia um número de 0 a 9999 e mostre na
            tela cada um dos dígitos separados.

                Ex: Digite um número: 1834
                  Unidade: 4
                  Dezena: 3
                  Centena: 8
                  Milhar: 1
"""

number = int(input('Digite um número (0 - 9999): '))
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

print('\n' + '-' * 30)
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
print('-' * 30)