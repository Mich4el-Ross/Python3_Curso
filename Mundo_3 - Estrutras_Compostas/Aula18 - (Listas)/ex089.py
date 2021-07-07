"""
Desafio 089

Problema: Crie um programa que leia nome e duas notas de vários alunos
          e guarde tudo em uma lista composta. No final, mostre um
          boletim contendo a média de cada um e permita que o usuário
          possa mostrar as notas de cada aluno individualmente.
"""

from time import sleep

final = []
student = []
grades = []
average = 0

while True:
    student.append(str(input('Nome: ')).title())
    grades.append(float(input('Nota 1: ')))
    grades.append(float(input('Nota 2: ')))

    student.append(grades[:])
    final.append(student[:])
    student.clear()
    grades.clear()

    opc = str(input('Deseja continuar ? [S/N]:')).strip().upper()

    while opc not in 'SN':
        print()
        print('\033[1;31mInsira corretamente os dados...\033[m')
        opc = str(input('Deseja continuar ? [S/N]: ')).strip().upper()

    print()

    if opc == 'N':
        print('-=-' * 14)
        break
    print('-=-' * 14)

print(f'{"ID" :<5} {"NOME" :<15} {"MÉDIA" :<5}')

for pos, x in enumerate(final):
    average = (final[pos][1][0] + final[pos][1][1]) / 2
    print(f'{pos :<5} {final[pos][0] :<15} {average :<6.2f}')

while True:
    print('-=-' * 14)
    num = int(input('Mostrar notas de qual aluno? [999 PARAR]: '))

    while 0 > num or num > len(final) - 1 and num != 999:
        print('\n\033[1;31mInsira corretamente os dados...\033[m')
        num = int(input('Mostrar notas de qual aluno? [999 PARA]: '))

    if num == 999:
        print('\n\033[1;31mFinalizando...\033[m')
        sleep(2)
        break

    print(f'\033[1mNotas de {final[num][0]} são {final[num][1]}\033[m')