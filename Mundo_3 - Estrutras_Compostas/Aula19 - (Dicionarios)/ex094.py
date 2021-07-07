"""
Desafio 094

Problema:   Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
            de cada pessoa em um dicionário e todos os dicionários em uma lista.
            No final, mostre:
                - Quantas pessoas foram cadastradas;
                - A média de idade do grupo;
                - Uma lista com todas as mulheres;
                - Uma lista com todas as pessoas com idade acima da média.
"""

group = list()
person = dict()
ages = 0

while True:
    print('-=-' * 15)
    person['Nome'] = str(input('Nome: ')).strip().capitalize()
    person['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()

    while person['Sexo'] not in 'MF':
        person['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()

    person['Idade'] = int(input('Idade: '))

    ages += person['Idade']
    group.append(person.copy())

    opc = str(input('Deseja continuar ? [S/N]: ')).strip().upper()

    while opc not in 'SN':
        print()
        print('\033[1;31mDados incorretos...\033[m')
        opc = str(input('Deseja continuar ? [S/N]: ')).strip().upper()

    print()

    if opc == 'N':
        break

print('-=-' * 15)
print(f' -- Foram cadastradas {len(group)} pessoas')
print(f' -- A média das idades é {ages / len(group) :.2f}')
print(f' -- Mulherers cadastradas: ', end='')

for x in group:
    if x['Sexo'] == 'F':
        print(f'{x["Nome"]};', end=' ')

print('\n -- Lista de pessoas acima da média: \n')

for idx, x in enumerate(group):
    if group[idx]['Idade'] > ages/len(group):
        print(f'Nome: {group[idx]["Nome"]};', end=' ')
        print(f'Sexo: {group[idx]["Sexo"]};', end=' ')
        print(f'Idade: {group[idx]["Idade"]};', end=' ' + '\n\n')

print('\033[1;31m --=-=- PROGRAMA ENCERRADO -=-=--\033[m')