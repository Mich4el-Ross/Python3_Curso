"""
Desafio 062

Problema: Melhore o DESAFIO 061, perguntando para o usuário se ele
          quer mostrar mais alguns termos. O programa encerra quando
          ele disser que quer mostrar 0 termos
"""

from time import sleep

a1 = int(input('Insira o primeiro termo dessa PA: '))
r = int(input('Insira a razão dessa PA: '))

cont = 1
terms = 10

while cont <= 10:
    print('{}'.format(a1), end=' ➙ ')
    a1 += r
    cont += 1
print('PAUSA')

opc = 1

while opc != 0:
    opc = int(input('\nQuantos termos deseja mostrar a mais ? '))
    print('')

    if opc != 0:
        cont = 1
        while cont <= opc:
            print('{}'.format(a1), end=' ➙ ')
            a1 += r
            cont += 1
            terms += 1
        print('PAUSA')
        sleep(1)
    else:
        print('\033[1;31mFinalizando...\033[m')
        sleep(2)

print('\n\033[1;32mA PA foi finalizada com sucesso, mostrando {} termos\033[m'.format(terms))