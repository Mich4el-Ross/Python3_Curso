"""
Desafio 022

Problema:   Crie um programa que leia o nome completo de uma pessoa
            e mostre:
                - O nome com todas as letras maiúsculas e minúscula;
                - Quantas letras o nome possui;
                - Quantas letras tem o primeiro nome.
"""

name1 = str(input('Digite seu nome completo: ')).strip()

print('\nAnalisando nome...')
print('Seu nome em maíusculas é {}'.format(name1.upper()))
print('Seu nome em minúsculas é {}'.format(name1.lower()))
print('Seu nome tem ao todo {} letras'.format(len(name1) - name1.count(' ')))
print('Seu primeiro nome tem {} letras'.format(name1.find(' ')))