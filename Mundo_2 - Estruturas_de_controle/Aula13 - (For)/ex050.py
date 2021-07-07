"""
Desafio 050

Problema: Desenvolva um programa que leia seus numeros inteiros e mostre
          a soma apenas daqueles que forem pares. Se o valor digitado for
          ímpar, desconsidere-o
"""

add = 0
for x in range(1, 7):
    num = int(input('Digite o {}° numero: '.format(x)))
    if num % 2 == 0:
        add += num
print('\nA soma entre os valores PARES digitados é {} '.format(add))