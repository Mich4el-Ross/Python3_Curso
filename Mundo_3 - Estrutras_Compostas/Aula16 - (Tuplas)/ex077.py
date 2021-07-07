"""
Desafio 077

Problema: Crie um programa que tenha uma tupla com várias palavras (NÃO USE ACENTOS)
          Depois disso, mostre quais são as vogais para cada palavra.
"""

print('-=-' * 15)
print(f'{"CONTANDO VOGAIS" :^45}')
print('-=-' * 15)

words = ('Programar', 'Python', 'Linguagem', 'Aplicativo', 'Sites',
         'Futuro', 'Cursos', 'Aprender', 'Mundo', 'Desafios')

vowels = ('a', 'e', 'i', 'o', 'u')

for pos, x in enumerate(words):
    print(f'\n{pos + 1 :2} ➙ Na palavra \033[4;31m{x.upper()}\033[m temos as vogais: ', end='')
    for letter in x:
        if letter in 'aeiou':
            print(f'\033[32m{letter}\033[m', end=' ')