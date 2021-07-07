"""
Desafio 061

Problema: Refaça o DESAFIO 051, lendo o primeiro número termo e
          a razão de uma PA, mostrando os 10 primeiros termos da
          progressão usando a estrutura WHILE.
"""

a1 = int(input('Insira o primeiro termo dessa PA: '))
r = int(input('Insira a razão dessa PA: '))

print('\nCom 1° termo = {} e razão = {}'.format(a1, r), end='')
print(', a nossa PA de 10 termos fica:')

cont = 1

while cont <= 10:
    print('{}'.format(a1), end=' ➙ ')
    a1 += r
    cont += 1
print('FIM')