"""
Desafio 033

Problema:   Faça um programa que leia três números e mostre qual é o
            maior e qual é o menor.
"""

n1 = int(input('Digite um valor para N1: '))
n2 = int(input('Digite um valor para N2: '))
n3 = int(input('Digite um valor para N3: '))

min_num = n1
max_num = n1

if n2 > n1 and n2 > n3:
    max_num = n2
if n3 > n1 and n3 > n2:
    max_num = n3

if n2 < n1 and n2 < n3:
    min_num = n2
if n3 < n1 and n3 < n2:
    min_num = n3

print('\n' + '-=-' * 10)
print('O maior valor digitado foi {}'.format(max_num))
print('O menor valor digitado foi {}'.format(min_num))
print('-=-' * 10)