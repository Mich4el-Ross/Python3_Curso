"""
Desafio 084:

Problema: Faça um programa que leia o nome e peso de várias pessoas.
          No final, mostre:
            - Quantas pessoas foram cadastradas;
            - Uma listagem com as pessoas mais pesadas;
            - Uma listagem com as pessoas mais leves;
"""

from time import sleep

group = list()
person = list()
cont = fat = thin = 0

print('-=-' * 15)
print(f'{"VERIFICADOR DE PESO" :^45}')
print('-=-' * 15 + '\n')

while True:

    person.append(str(input('Nome: ')))
    person.append(float(input('Peso: ')))

    if len(group) == 0:
        fat = thin = person[1]
    else:
        if person[1] > fat:
            fat = person[1]
        elif person[1] < thin:
            thin = person[1]

    group.append(person[:])
    person.clear()
    cont += 1

    opc = str(input('Deseja continuar ? [S/N]: ')).upper().strip()

    while opc not in 'SN':
        print()
        print('Insira corretamente os dados...')
        opc = str(input('Deseja continuar ? [S/N]: ')).upper().strip()

    print()

    if opc == 'N':
        print('\033[1;31mFinalizando...\033[m')
        sleep(3)
        break
    print('-=-' * 15)

print('\n' + '-=-' * 30)
print(f'Foram cadastradas {cont} pessoas no total.')
print(f'O maior peso registrado foi {fat}Kg correspondendo aos pesos de ', end='')
for p in group:
    if p[1] == fat:
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso registrado foi {thin}Kg correspondendo aos pesos de ', end='')
for p in group:
    if p[1] == thin:
        print(f'[{p[0]}]', end=' ')

print('\n' + '-=-' * 30)