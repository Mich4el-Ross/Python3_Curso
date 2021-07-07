"""
Desafio 037

Problema: Escreva um programa em Python que leia um número inteiro qualquer
          e peça para o usuário escolher qual  será a base de conversão:
          1 para binário, 2 para octal e 3 para hexadecimal.
"""

num = int(input('Digite um numero inteiro: '))
print('')

print('-=-'*11)
print('Escolha uma base para converter')
print('[1] --> Binário')
print('[2] --> Octal')
print('[3] --> Hexadecimal')
print('-=-'*11)

opc = int(input('Sua opção: '))
print('')

if opc == 1:
    print('O numero {} em BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('O numero {} em OCTAL é {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('O numero {} em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Escolha uma opção válida.')