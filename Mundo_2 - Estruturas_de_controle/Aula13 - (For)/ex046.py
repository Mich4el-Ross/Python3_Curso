"""
Desafio 046

Problema: Faça um programa que mostre a tela de contagem regressiva para o estouro
          de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre
          eles.
"""

from time import sleep

print('-=-'*10)
print('{:^30}'.format('O ano novo começa em '))

for x in range(10, -1, -1):
    print(x)
    sleep(1)
print('{:^30}'.format('FELIZ ANO NOVOO'))