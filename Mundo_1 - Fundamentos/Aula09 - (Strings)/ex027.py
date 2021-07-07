"""
Desafio 027

Problema:       Faça um programa que leia o nome completo de uma pessoa,
                mostrando em seguida o primeiro e o último nome.
"""

name = str(input('Digite seu nome (completo): ')).strip().split()

print('Seu primeiro nome é: {}'.format(name[0]))
print(len(name))
print('Seu último nome é: {}'.format(name[len(name) - 1]))