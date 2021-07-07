"""
Desafio 004

Problema:   Faça um programa que leia algo pelo teclado e mostre
            na tela o seu tipo primitivo e todas as informações
            possíveis sobre ele.
"""


X = (input('Digite algo: '))
print('O tipo primitivo desse valor é ',type(X))

print('')
print('Alfabetico:', X.isalpha())
print('Alfanúmerico:', X.isalnum())
print('Númerico:', X.isnumeric())
print('Maiúsculo:', X.isupper())
print('Minúsculo:', X.islower())
print('É capitalizada:', X.istitle())
print('Só tem espaços:', X.isspace())