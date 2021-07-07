"""
Desafio 095

Problema: Aprimore o desafio 093 para que ele funcione com vários jogadores,
          incluindo um sistema de visualização de detalhes do aproveitamento
          de cada jogador.
"""

group = list()
player = dict()
gols = list()

while True:
    print('-=-' * 15)
    player['Nome'] = str(input('Nome do jogador: ')).title()
    matches = int(input(f'Quantas partidas {player["Nome"]} jogou: '))
    print('')

    for x in range(matches):
        gols.append(int(input(f'\tGols na {x + 1}° partida: ')))

    player['Gols'] = gols[:]
    player['Total'] = len(gols)

    group.append(player.copy())
    player.clear()
    gols.clear()

    print('')
    resp = input('Deseja continuar ? [S/N]: ').strip().upper()

    while resp not in 'SN':
        print()
        print('\033[1;31mDados incorretos...\033[m')
        resp = input('Deseja continuar ? [S/N]: ').strip().upper()
    print()

    if resp == 'N':
        break

print('-=-' * 15)
print(f'{"ID":<3} {"NOME":<17} {"GOLS":<17} {"TOTAL":<5}')
for ref, info in enumerate(group):
    print(f'{ref:<3}', end='')
    for v in info.values():
        print(f'{str(v):<18}', end='')
    print()

while True:
    print('-=-' * 15)
    opc = int(input('Mostrar dados de qual jogador? [999 PARA]: '))
    print()

    while 0 > opc or opc > len(group) - 1 and opc != 999:
        print('\033[1;31mInsira corretamente os dados...\033[m')
        opc = int(input('Mostrar notas de qual aluno? [999 PARA]: '))
        print()

    if opc == 999:
        break

    print(f'\033[1;36m-- LEVANTAMENTO DO {group[opc]["Nome"]}\033[m')
    for idx, x in enumerate(group[opc]["Gols"]):
        print(f'No jogo {idx} fez {x} gols.')

print('\033[1;31m --=-=- PROGRAMA ENCERRADO -=-=--\033[m')
