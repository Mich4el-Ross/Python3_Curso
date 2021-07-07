"""
Desafio 091

Problema:  Crie um programa onde quatro jogadores joguem um dado e tenham resultados aleatórios.
           Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
           sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter

ranking = list()
rounds = {
    'Jogador_1': randint(1, 6),
    'Jogador_2': randint(1, 6),
    'Jogador_3': randint(1, 6),
    'Jogador_4': randint(1, 6)
}

print('Valores sorteados: ')

for k, v in rounds.items():
    print(f' O {k} tirou {v}')
    sleep(0.5)

ranking = sorted(rounds.items(), key=itemgetter(1), reverse=True)

print()
print(f'=-=-=-=-=-- RANKING --=-=-=-=-=')

for k, v in enumerate(ranking):
    print(f' {k + 1}° Lugar - {v[0]} com {v[1]}')
    sleep(0.5)