"""
Desafio 038

Problema: Escreva um programa que leia dois números inteiros e compare-os.
          mostrando na tela uma mensagem:
          - O primeiro valor é maior
          - O segundo valor é maior
          - Não existe valor maior, os dois são iguais
"""

num_1 = float(input('Insira um  valor para n1: '))
num_2 = float(input('Insira outro para n2: '))
print('')

print('-=-'*13)

if num_1 > num_2:
    print('O PRIMEIRO valor digitado é o MAIOR'.format(num_1))
elif num_2 > num_1:
    print('O SEGUNDO valor digitado  é o  MAIOR'.format(num_2))
else:
    print('Os valores digitados são IGUAIS')

print('-=-'*13)