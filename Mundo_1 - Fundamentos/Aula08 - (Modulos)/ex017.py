"""
Desafio 017

Problema:   Faça um programa que leia o comprimento do cateto oposto e do
            cateto adjacente de um triângulo, calcule o mostre o comprimento
            da hipotenusa.
"""

from math import hypot

print('-'*50+'\n')
ca = float(input('Digite o comprimento do cateto adjacente: '))
co = float(input('Digite o comprimento do cateto oposto: '))
hip = hypot(ca, co)
print('A hipotenusa desse triangulo vale: {:.2f}'.format(hip))