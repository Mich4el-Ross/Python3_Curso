"""
Desafio 100

Problema: Faça um programa que tenham uma lista chamada numeros e duas funções chamadas
          sorteia() e somaPar().

          A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a
          segunda função vai mostrar a soma entre todos valores pares sorteados
          pela função anterior.
"""

from random import randint
from time import sleep


def sortear():
    values = []

    for x in range(0, 5):
        values.append(randint(1, 10))

    print('Sorteando 5 valores da lista: ', end='')

    for y in values:
        print(y, end=' ')
        sleep(0.5)
    else:
        print('Pronto!')

    somapar(values)


def somapar(num):
    add = 0

    for x in num:
        if x % 2 == 0:
            add += x
    print(f'Somando os valores pares de {num}, temos {add}')


print('-=-' * 10 + f'\n{"SORTEIO DE NUMEROS" :^30}\n' + '-=-' * 10 + '\n')

sortear()
