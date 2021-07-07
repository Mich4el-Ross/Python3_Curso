"""
Desafio 053

Problema: Crie um programa que leia uma frase qualquer e diga se ela é um
          PALINDROMO, desconsiderando-o os espaços.
"""

phrase = str(input('Digite uma frase para analisar: ')).strip().upper()
divided = phrase.split()
words = ''.join(divided)
inverse = ''

print('')

for x in range(len(words) - 1, -1, -1):
    inverse += words[x]

print('Voce digitou: {}'.format(phrase))
print('{} invertido fica como {}'.format(words, inverse))

if words == inverse:
    print('Elas são iguais, portanto temos um \033[1;32mPALINDROMO\033[m')
else:
    print('Essa é uma frase \033[1;33mNORMAL\033[m')