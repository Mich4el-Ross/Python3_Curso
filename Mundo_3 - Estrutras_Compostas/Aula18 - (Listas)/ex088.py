"""
Desafio 088

Problema: Faça um programa que ajude um jogador da mega sena a criar palpites.
          O programa vai perguntar quantos jogos serão gerados e vai sortear
          6 números entre 1 e 60 para cada jogo. No final mostre os palpites.

          OBS: Deve ser usado listas compostas
"""

from time import sleep
from random import randint

numbers = []
hunches = []

print('-=-' * 12)
print(f'{"MEGA SENA" :^36}')
print('-=-' * 12 + '\n')

games = int(input('Digite quantos jogos deseja: '))

for x in range(0, games):
    for y in range(0, 6):
        num = randint(1, 60)

        if num not in hunches:
            hunches.append(num)
        else:
            num = randint(1, 60)
            hunches.append(num)
    hunches.sort()
    numbers.append(hunches[:])
    hunches.clear()

print()
print('-=--=--=--=- SORTEANDO -=--=--=--=-')
for z in range(0, games):
    print(f'Jogo {z+1}:  {numbers[z]}')
    sleep(0.5)
print('-=--=--=-- < BOA SORTE > -=--=--=--')