"""
Desafio 093:

Problema:   Crie um programa que gerencie o aproveitamento de um jogador de futebol.
            O programa vai ler o nome do jogador e quantas partidas ele jogou.
            Depois vai ler a quantidade de gols feitos em cada partida.
            No final, tudo isso será guardado em um dicionário, incluindo o total de gols
            feitos durante o campeonato.
"""

player = dict()
gols = list()

player['Nome'] = str(input('Qual o nome do jogador: ')).strip().capitalize()
matches = int(input(f'Quantos jogos {player["Nome"]} jogou: '))
print()

for x in range(matches):
    gols.append(int(input(f'Gols na {x+1}° partida: ')))

player['Gols'] = gols[:]
player['Total'] = sum(gols)

print('\n' + '-=-' * 10)

for k, v in player.items():
    print(f'{k} = {v}')

print('-=-' * 10)

print(f'{player["Nome"]} jogou {matches} jogos.')

for idx, x in enumerate(gols):
    print(f' --> Na partida {idx + 1}, fez {x} gols')
print(f'Foi um total de {sum(gols)} gols')