"""
Desafio 015

Problema:   Escreva um programa que pergunte a quantidade de Km rodados
            por um carro alugado e a quantidade de dias pelos quais ele
            foi alugado. Calcule o preço a pagar, sabendo que o carro
            custa R$ 60 por dia e R$ 0,15 por Km rodado.
"""

days = int(input('Quantos dias alugados: '))
km = float(input('Quantos Km rodados: '))

rent= (days * 60) + (km * 0.15)

print('\nO valor do aluguel do carro é de: R$ {:.2f}'.format(rent))