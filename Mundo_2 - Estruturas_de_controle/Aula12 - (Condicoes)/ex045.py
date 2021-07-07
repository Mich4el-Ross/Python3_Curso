"""
Desafio 044

Problema: Faça o computador jogar Jokenpô com o usuário
"""

from random import randint
from time import sleep

print('-=-'*10)
print('{:^30}'.format('OPÇÕES'))
print('[1] --> PEDRA')
print('[2] --> PAPEL')
print('[3] --> TESOURA')
print('-=-'*10)

#ESCOLHA DAS JOGADAS
plays = ('Pedra', 'Papel', 'Tesoura')
computer = randint(0, 2)
user = int(input('Sua escolha: ')) - 1

print('')

# VALIDAR O JOGO
if user > 2:
    print('-' * 30)
    print('\033[1;31m ESCOLHA UMA OPÇÃO VÁLIDA!! \033[m')
#JO - KEN - PÔ!
else:
    print('\033[1;31mJO\033[m ', end='')
    sleep(1)
    print('\033[1;33mKEN\033[m ', end='')
    sleep(1)
    print('\033[1;32mPÔ!\033[m')
    print('\n' + '-' * 30)

    #Caso de EMPATE
    if user == computer:
        print('\033[1;33m{:^30}\033[m'.format('EMPATE'))

    #Caso user escolher PEDRA
    elif user == 0 and computer == 2:
        print('\033[1;32m{:^30}\033[m'.format('USER WINS'))
    elif user == 0 and computer == 1:
        print('\033[1;31m{:^30}\033[m'.format('COMPUTER WINS'))

    #Caso user escolher PAPEL
    elif user == 1 and computer == 0:
        print('\033[1;32m{:^30}\033[m'.format('USER WINS'))
    elif user == 1 and computer == 2:
        print('\033[1;31m{:^30}\033[m'.format('COMPUTER WINS'))

    #Caso user escolher TESOURA
    elif user == 2 and computer == 1:
        print('\033[1;32m{:^30}\033[m'.format('USER WINS'))
    elif user == 2 and computer == 0:
        print('\033[1;31m{:^30}\033[m'.format('COMPUTER WINS'))

    print('Jogador: \033[1m{}\033[m'.format(plays[user].upper()))
    print('Computador: \033[1m{}\033[m'.format(plays[computer].upper()))

print('-' * 30)