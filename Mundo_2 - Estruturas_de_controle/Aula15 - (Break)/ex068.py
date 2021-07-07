"""
Desafio 068

Problema: Faça um programa que jogue PAR ou ÍMPAR com o computador. O jogo
          só será interrompido quando o jogador perder, mostrando o total
          de vitórias consecutivas que ele consquistou
"""

from random import randint
cont = 0

print('-=-' * 10)
print('{:^30}'.format('PAR OU IMPAR'))

while True:
    print('\n' +'-=-' * 10)
    user_value = int(input('Digite um valor: '))
    user = str(input('Par ou Ímpar ? [P/I]: ')).strip().upper()

    computer = randint(1, 10)

    #Validar JOGO
    while user != 'P' and user != 'I':
        print('Opção inválida. Informe novamente...')
        user = str(input('Par ou Ímpar ? [P/I]: ')).strip().upper()

    result = user_value + computer

    print('-=-' * 10)
    print(f'Voce jogou {user_value} e o computador {computer}')
    print(f'O resultado é {result}', end=' ➙ ')

    if result % 2 == 1:
        print('DEU IMPAR')
        print('-=-' * 10)
        if user == 'I':
            print('\n\033[1;32mVOCÊ GANHOU essa rodada\033[m')
            cont += 1
        else:
            print('\n\033[1;31mVOCE PERDEU!\033[m')
            break
    else:
        print('DEU PAR')
        print('-=-' * 10)
        if user == 'P':
            print('\n\033[1;32mVOCÊ GANHOU essa rodada\033[m')
            cont += 1
        else:
            print('\n\033[1;31mVOCE PERDEU!\033[m')
            break

print('\n' + '=-=' * 13)
print(f'\033[1;31mGAME OVER!\033[m Você venceu {cont} veze(s) seguida(s) ')
print('=-=' * 13)