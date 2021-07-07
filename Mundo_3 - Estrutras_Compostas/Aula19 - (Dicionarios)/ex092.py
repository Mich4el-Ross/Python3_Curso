"""
Desafio 092

Problema:   Crie um programa que leia nome, ano de nascimento e carteira de trabalho
            de uma pessoa e cadastre-os (com idade) em um dicionário se por acaso a CTPS
            (Carteira de Trabalho e Previdência Social) for diferente de ZERO, o dicionário
            receberá também o ano de contratação e o salário. Calcule e acrescente, além da
            idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import date
year = date.today().year
person = dict()

person['Nome'] = str(input('Nome: ')).strip()
person['Idade'] = int(input('Ano de Nascimento: '))
person['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))


if person['CTPS'] != 0:
    person['Ano_Contratação'] = int(input('Ano de Contratação: '))
    person['Salário'] = float(input('Salário atual: R$ '))

    person['Aposentadoria'] = person['Ano_Contratação'] + 35 - person['Idade']

if person['CTPS'] == 0:
    person['CTPS'] = 'Não possui'

person['Idade'] = year - person['Idade']

print('\n' + '-=-' * 12)

for k, v in person.items():
    print(f'{k}: {v}')

print('-=-' * 12)
