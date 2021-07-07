"""
Desafio 006

Problema:   Crie um algoritmo que leia um número e mostre o
            seu dobro, triplo e raiz quadrada.
"""

n = int(input('Digite um numero: '))

print('\nO dobro de {} e {}'.format(n, (n*2)))
print('O triplo de {} e  {}'.format(n, n*3))
print('A raiz quadrada de {} e {:.2f}'.format(n, n**0.5))