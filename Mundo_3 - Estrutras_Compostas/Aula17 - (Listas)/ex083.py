"""
Desafio 083

Problema: Crie um programa onde o usuário digite uma expressão qualquer e use
          parênteses. O programa deverá analisar se a expressão passada está
          com os parênteses abertos e fechados na ordem correta.
"""

character = []
expression = str(input('Digite sua expressão: '))

for simbols in expression:
    if simbols == '(':
        character.append('(')
    elif simbols == ')':
        if len(character) > 0:
            character.pop()
        else:
            character.append(')')
            break

if len(character) == 0:
    print('Expressão correta...')
else:
    print('Expressão incorreta...')




