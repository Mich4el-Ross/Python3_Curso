"""
Desafio 052

Problema: Faça uim programa que leia um número e diga se ele é ou não um
          número primo
"""

num = int(input('Digite um numero: '))
cont = 0
print('')

for x in range(1, num + 1):
    if num % x == 0:
        print('\033[32m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(x), end='')

print('\n\n\033[mO número foi divisível \033[1;36m{} vezes\033[m , '.format(cont), end='')

if cont == 2:
    print('logo ele \033[32mÉ PRIMO!\033[m')
else:
    print('logo ele \033[31mNÃO É PRIMO!\033[m')