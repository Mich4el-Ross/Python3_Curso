"""
Desafio 028

Problema:   Escreva um programa que faça o computador "pensar" em um número
            inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
            foi o número escolhido pelo computador.
            O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

import random
from time import sleep

print('\n'+'-=-'*18)
print('Vou pensar em um numero entre 0 e 5. Tente acertar...')
print('-=-'*18)

machine = random.randint(0,5)
player = int(input('\nQual a sua escolha ?' ))

print('PROCESSANDO...')
sleep(2)
if player == machine:
    print('\nPARABÉNS! você me venceu')
else:
    print('\nHAHA, GANHEI... Eu pensei no número {} e não no {}'.format(machine, player))