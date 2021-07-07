"""
Desafio 005

Problema:   Faça um programa que leia um número inteiro e mostre
            na tela o seu sucessor e seu antecessor.
"""


n = int(input('Digite um numero: '))

print('\nO sucessor do numero {} e: {}'.format(n, n+1))
print('O antecessor do numero {} e: {}'.format(n, n-1))