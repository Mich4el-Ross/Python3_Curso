"""
Desafio 011

Problema:   Faça um programa que leia a largura e altura de uma parede
            em metros, calcule a sua área e a quantidade de tintas
            necessárias para pintá-la, sabendo que cada litro de tinta
            pinta uma área de 2m².
"""

width = float(input('Digite a largura da parede (m): '))
height = float(input('Digite a altura da parede (m): '))

area = width * height
qnt = area / 2

print(' \nSua parede tem dimensões de {} x {} e sua área e de {} metros quadrados'.format(width, height, area))
print('Voce irá precisar de {:.4f}L de tinta.'.format(qnt))