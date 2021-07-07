"""
Desafio 007

Problema:   Desenvolva um programa que leia as duas notas de um
            aluno, calcule e mostre a sua média.
"""

nome = input('Digite seu nome: ')
n1 = float(input('Digite sua 1° nota: '))
n2 = float(input('Digite sua 2° nota: '))
med = (n1+n2)/2

print('\nA media de {} e de {:2}'.format(nome, med))