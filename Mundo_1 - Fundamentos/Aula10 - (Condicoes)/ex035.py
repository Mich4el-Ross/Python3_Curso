"""
Desafio 035

Problema:   Desenvolva um programa que leia o comprimento de três retas e diga
            ao usuário se elas podem ou não formar um triângulo.
"""

a = float(input('Digite o valor para a primeira reta (a): '))
b = float(input('Digite o valor para a segunda reta (b): '))
c = float(input('Digite o valor para a terceira reta (c): '))

if a < b+c and b < a+c and c < a+b:
    resp = 'É'
else:
    resp = 'Não é'

print('\n'+'-=-' * 15)
print('Para os valores de a = {} b = {} e c = {}'.format(a, b, c))
print('{} possivel formar um triângulo'.format(resp))
print('-=-' * 15)