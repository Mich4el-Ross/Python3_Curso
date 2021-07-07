"""
Desafio 069

Problema: Crie um programa que leia a idade e o sexo de varias pessoas. A cada
          pessoa cadastrada, o programa pergunta se o usuario quer continuar ou
          não.
          No final mostre:
          - Quantas pessoas tem mais de 18 anos
          - Quantos homens foram cadastrados
          - Quantas mulheres têm menos de 20 anos
"""

cont18 = cont20 = men = 0

print('-=--=- CADASTRO DE PESSOAS -=--=-' + '\n')
while True:

    print('-=-' * 10)
    age = int(input('Idade: '))
    genre = str(input('Sexo [M/F]: ')).strip().upper()

    #Validar gênero
    while genre != 'M' and genre != 'F':
        print('\033[1;31mDado INVÁLIDO...Insira novamente\033[m')
        genre = str(input('Sexo [M/F]: ')).strip().upper()

    print('-=-' * 10)

    if genre == 'M':
        men += 1
    if age == 18:
        cont18 += 1
    if genre == 'F' and age <20:
        cont20 += 1

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar ? [S/N]: ')).strip().upper()

    if opc == 'N':
        break

print('\n' + '-=-'*16)
print('Foram cadastradas {} pessoas maiores de 18 anos'.format(cont18))
print('Foram cadastrados {} homens'.format(men))
print('Temos um total de {} mulheres abaixo dos 20 anos'.format(cont20))
print('-=-'*16)