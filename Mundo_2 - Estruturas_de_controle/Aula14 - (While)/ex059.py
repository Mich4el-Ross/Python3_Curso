"""
Desafio 059

Problema: Crie um programa que leia dois valores e mostre um menu de
          opções na tela:

          [1] - Somar
          [2] - Multiplicar
          [3] - Maior
          [4] - Novos números
          [5] - Sair do programa

          O programa deverá realizar a operação solicidade em cada
          caso.
"""

from time import sleep
num_1 = int(input('Insira o 1° valor: '))
num_2 = int(input('Insira o 2° valor: '))

menu = """
-=-=-=-=- MENU -=-=-=-=-
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa
"""

opc = 0

while opc != 5:

    print(menu)
    opc = int(input('---> Escolha uma opção: '))
    print('')

    if opc == 1:
        print('O resultado de {} + {} é = {}'.format(num_1, num_2, num_1 + num_2))
    elif opc == 2:
        print('O resultado de {} X {} é = {}'.format(num_1, num_2, num_1 * num_2))
    elif opc == 3:
        if num_1 == num_2:
            print('Os valores digitados são IGUAIS')
        else:
            print('O MAIOR valor digitado é {}'.format(max(num_1, num_2)))
    elif opc == 4:
        print('Informe os números novamente')
        num_1 = int(input('Insira o 1° valor: '))
        num_2 = int(input('Insira o 2° valor: '))
    elif opc == 5:
        print('\033[31mFinalizando...\033[m')
        sleep(3)
    else:
        print('Digite uma opção \033[1;31mVÁLIDA!\033[m')

    sleep(2)

print('\n\033[1;32mO PROGRAMA FOI ENCERRADO COM SUCESSO!\033[m')