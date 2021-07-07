"""
Desafio 024

Problema:   Crie um programa que leia o nome de uma cidade e diga se ela
            começa ou não com o nome ‘SANTO’
"""

city = str(input('Digite o nome de uma cidade: ')).strip().upper().split()

print('O nome da cidade digitada começa com SANTO ? {}'.format(city[0] == 'SANTO'))