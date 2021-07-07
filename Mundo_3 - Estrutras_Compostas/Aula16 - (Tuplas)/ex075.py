"""
Desafio 075

Problema: Desenvolva um programa que leia quatro valores pelo teclado
          e guarde-os em uma tupla.
          No final, mostre:

            - Quantas vezes apareceu o valor 9;
            - Em que posição foi digitado o primeiro valor 3;
            - Quais foram os números pares.
"""

print('-=-' * 10)
print(f'{"ANÁLISE DE DADOS" :^30}')
print('-=-' * 10)

numbers = ()
for x in range(1, 5):
    numbers += int(input(f'Digite o {x}° número: ')),

print('\n' + '-=-' * 16)
print(f'Os valores digitados foram: {numbers}')
print(f'O numero 9 apareceu {numbers.count(9)} vezes')

if 3 in numbers:
    print(f'O primeiro 3 apareceu {numbers.index(3)}° posição')
else:
    print('O número 3 não foi digitado em nenhuma posição')


print('Pares digitados: ', end='')
for evens in numbers:
    if evens % 2 == 0:
        print(evens, end=' ')
print('\n' + '-=-' * 16)