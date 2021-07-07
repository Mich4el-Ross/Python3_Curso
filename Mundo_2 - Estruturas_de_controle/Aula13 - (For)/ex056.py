"""
Desafio 056

Problema: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No
          final do programa mostre:
          - A media da idade do grupo
          - Qual o nome do homem mais velho
          - Quantas mulheres têm menos de 20 anos
"""

average = 0
cont = 0
older = 0
man = ''

for x in range(1, 5):
    print('-=-=- {}° Pessoa -=-=-'.format(x))
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    genre = str(input('Sexo [M/F]: ')).strip().upper()

    average += age

    if genre == 'M':
        if age > older:
            older = age
            man = name
    else:
        if age < 20:
            cont += 1

print('\n' + '-=-'*17)
print('A média da idade do grupo registrada é: {:.1f} anos'.format(average/4))
print('O homem mais velho se chama {} e possui {} anos'.format(man, older))
print('Temos um total de {} mulheres abaixo dos 20 anos'.format(cont))
print('-=-'*17)