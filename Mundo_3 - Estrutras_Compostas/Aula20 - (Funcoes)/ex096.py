"""
Desafio 096

Problema: Faça um programa que tenha uma função chamada area() e que receba as
            dimensões de um terreno retangular  e mostre ao final a sua area.
"""

def area(width, lenght):
    a = width * lenght
    print(f'\nA área de um terreno de {width} x {lenght} é de {a}m²')


print('-=-' * 7 + '\n Controle de Terreno \n' + '-=-' * 7)
wid = float(input('\nDigite a largura (m): '))
len = float(input('Digite o comprimento (m): '))

area(wid, len)