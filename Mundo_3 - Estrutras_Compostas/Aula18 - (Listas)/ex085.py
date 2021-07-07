"""
Desafio 085

Problema: Crie um programa para o usuário digitar sete valores númericos e
          cadastre-os em uma única lista que mantenha separados os valores
          pares e ímpares. No final, em ordem crescente.
"""

numbers = [[], []]

print('-=-' * 15)
print(f'{"PARES E ÍMPARES" :^45}')
print('-=-' * 15 + '\n')

for x in range(0, 7):
    value = int(input(f'Insira o {x+1}° valor: '))

    if value % 2 == 0:
        numbers[0].append(value)
    if value % 2 == 1:
        numbers[1].append(value)

numbers[0].sort()
numbers[1].sort()

print('\n' + '-=-' * 15)
print(f'Valores PARES digitados: {numbers[0]}')
print(f'Valores ÍMPARES digitados: {numbers[1]}')
print('-=-' * 15)
