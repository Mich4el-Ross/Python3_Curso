"""
Desafio 019

Problema:   Um professor quer sortear um dos seus quatro alunos para apagar
            o quadro. Faça um programa que ajude ele, lendo o nome deles e
            escrevendo o nome do escolhido
"""

import random
n1 = input('Aluno 1:')
n2 = input('Aluno 2:')
n3 = input('Aluno 3:')
n4 = input('Aluno 4:')

X = random.choice([n1, n2, n3, n4])

print('-' * 50)
print('O aluno selecionado pelo professor foi {}'.format(X))
print('-' * 50)