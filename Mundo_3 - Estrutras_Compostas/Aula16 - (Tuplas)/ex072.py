"""
Desafio 072

Problema: Crie um programa que tenha uma tupla totalmente preenchida com
          uma contagem por extenso, de zero até vinte. O programa deverá
          ler um número, e mostra-lo por extenso
"""

from time import sleep
numbers = ('zero', 'um', 'dois', 'três', 'quarto', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

print('-=-' * 12)
print(f'{"SUPER CONTADOR" :^36}')
print('-=-' * 12 + '\n')

while True:
    num = int(input('Digite um número entre 0 e 20: '))

    while num < 0 or num > 20:
        print('\n' + '-=-' * 12)
        print(f'\033[1;31mInforme os dados corretamente...\033[m')
        num = int(input('Digite um número entre 0 e 20: '))
        print('-=-' * 12)

    print('\n' + '-=-' * 12)
    print(f'Você digitou o número {numbers[num]}'.upper())
    print('-=-' * 12 + '\n')

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar [S/N]: ')).upper().strip()

    if opc == 'N':
        print('\033[1;31mFinalizando...\033[m')
        sleep(3)
        break

print(f'\n\033[1;32mPROGRAMA ENCERRADO\033[m')