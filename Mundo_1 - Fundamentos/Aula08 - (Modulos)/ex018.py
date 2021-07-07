"""
Desafio 018

Problema:   Faça um programa que leia um ângulo qualquer a mostre na
            tela o valor do seno, cosseno e tangente desse ângulo.
"""

from math import sin, cos, tan, radians
ang = float(input('Digite um angulo:'))
sin = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O seno vale {:.2f}\nO cosseno é {:.2f}\nA tangente e {:.2f}'.format(sin, cos, tan))