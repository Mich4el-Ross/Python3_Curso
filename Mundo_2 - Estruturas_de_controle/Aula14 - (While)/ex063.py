"""
Desafio 063

Problema: Escreva um programa que leia um numero N inteiro e qualquer
          mostre na tela os N primeiros elementos de uma Sequencia de
          Fibonacci
"""

print('-=-'*10)
print('{:^30}'.format('SEQ. FIBONACCI'))
print('-=-'*10)

num = int(input('\nInsira quantos termos você deseja mostrar: '))

T1 = 0
T2 = 1
cont = 1

print('')
print('{} ➙ {} ➙ '.format(T1, T2), end='')

while cont <= num:
    T3 = T1 + T2
    print('{}'.format(T3), end=' ➙ ')
    T1 = T2
    T2 = T3

    cont += 1
print('FIM')