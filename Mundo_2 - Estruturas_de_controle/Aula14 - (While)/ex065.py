"""
Desafio 065

Problema: Crie um programa que leia vários números inteiros.No final da
          execução, mostre a média entre todos os valores e qual foi o
          maior e menor valor lido. O programa deve perguntar ao usuário
          se ele quer ou não continuar
"""

resp = 'S'
cont = add = 0

while resp == 'S':
    number = int(input('Digite um número: '))

    add += number
    cont += 1

    if cont == 1:
        big = less = number
    else:
        if number >= big:
            big = number
        if number <= less:
            less = number

    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()

med = add / cont

print('\n' + '-=-'*14)
print('Voce digitou {} números e a média é {:.2f}'.format(cont, med))
print('O MAIOR valor é {} e o MENOR é {}'.format(big, less))
print('-=-'*14)