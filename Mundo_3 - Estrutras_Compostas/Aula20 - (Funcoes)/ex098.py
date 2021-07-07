"""
Desafio 098

Problema: Faça um programa que tenha uma função chamada contador(), que receba três
          parâmetros: inicio, fim e passo e realize a contagem.

          Seu programa tem que realizar três contagens atráves da função criada:
            - De 1 até 10, de 1 em 1
            - De 10 até 0, de 2 em 2
            - Uma contagem personalizada
"""

from time import sleep


def contador(inicio, fim, passo):
    print('-=-' * 14)
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1

    print(f'Contando de {inicio} até {fim} de {passo} em {passo}')

    if fim > inicio:
        for x in range(inicio, fim + 1, passo):
            print(x, end=' ')
            sleep(0.5)
        print('FIM!')
    else:
        passo *= -1
        for x in range(inicio, fim - 1, passo):
            print(x, end=' ')
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-=-' * 14)
print('Agora é sua vez de personalizar a contagem!')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)


