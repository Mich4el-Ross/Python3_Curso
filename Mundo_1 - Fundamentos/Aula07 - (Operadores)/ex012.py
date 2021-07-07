"""
Desafio 012

Problema:   Faça um algoritmo que leia o preço de um produto e
            mostre seu novo preço, com 5% de desconto.
"""

prod = float(input('Qual o preço do produto que deseja comparar ? R$'))

desc = prod * 5/100

print('\n'+'-'*50)
print('Voce recebeu um desconto de R$ {:.2f}'.format(desc))
print('Voce ira pagar nesse produto o valor de R${:.2f}'.format(prod - desc))
print('-'*50)