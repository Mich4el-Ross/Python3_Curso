"""
Desafio 010

Problema:   Crie um programa que leia quanto dinheiro uma pessoa tem
            na carteira e mostre quantos dólares ela pode comprar.

            Considere US$ 1,00 = R$ 3,27
"""

din = float(input('Quanto de dinheiro vc tem na sua carteira ? R$ '))
con = din / 3.27

print('Com R${} vc consegue trocar por  US${:.2f} '.format(din, con))