"""
Desafio 067

Problema: Faça um programa que mostre a tabuada de vários números,
          para cada valor digitado pelo usuário. O programa será
          interrompido quando o número solicitado for negativo
"""

from time import sleep
res = 0

while True:

    print('-=-' * 14)
    num = int(input('Deseja saber a tabuada de que número: '))
    print('-=-' * 14)

    if num < 0:
        print('\n\033[1;31mFinalizando...\033[m')
        sleep(2)
        break

    for x in range (1, 11):

        print(f'{num} X {x:2} = {res}')
        x += 1
        res = num * x

print('\n' + '\033[1;36m-=-\033[m'*12)
print('\033[1;32mPROGRAMA ENCERRADO COM SUCESSO\033[m')
print('\033[1;32m{:^31}\033[m'.format('VOLTE SEMPRE!'))
print('\033[1;36m-=-\033[m'*12)