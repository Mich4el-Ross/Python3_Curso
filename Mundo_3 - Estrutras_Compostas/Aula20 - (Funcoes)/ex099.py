"""
Desafio 099

Problema: Faça um programa que tenha a função maior(), e que recebe vários parâmetros
          com valores inteiros. No final mostre o maior valor informado

"""

from time import sleep

def maior(* num):
    lenght = len(num)
    cont = 0
    value = 0

    print('-=-' * 15 + '\nAnalisando os valores passados...')

    for x in num:
        print(x, end=' ')
        sleep(1)

        if cont == 0:
            value = x
        else:
            if x > value:
                value = x
        cont += 1

    print(f'Foram informados {lenght} valores')
    print(f'O maior valor informado foi {value}.')

maior(4, 7, 2, 5, 3)
maior(6, 0, 2, 4)
maior(3, 8)
maior(2)
maior()
