"""
Desafio 025

Problema:   Crie um programa que leia o nome de uma pessoa e diga se ela
            tem ‘SILVA’ no nome.
"""

name = str(input('Digite seu nome:')).strip().upper()

print('Seu nome tem SILVA ? : {}'.format('SILVA' in name))