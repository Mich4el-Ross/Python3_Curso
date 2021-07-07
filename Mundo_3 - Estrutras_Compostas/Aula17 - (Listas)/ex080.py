"""
Desafio 080

Problema: Crie um programa onde o usuário insira 5 valores númericos e os cadastre
          em uma lista, já na posição correta de inserção (sem usar o sort()).
          No final, mostre a lista.
"""

values = []

for x in range(0, 5):
    num = int(input('Insira um número:'))

    while num in values:
        print('-=-' * 15)
        print('Valor duplicado. Tente novamente...')
        num = int(input('Insira um número:'))
        print()

    if x == 0 or num > values[-1]:
        values.append(num)
        print('Valor adicionado no final da lista')
    else:
        pos = 0
        while pos < len(values):
            if num <= values[pos]:
                values.insert(pos, num)
                print(f'Valor adicionado na {pos}° posição')
                break

                pos += 1
    print()

print('-=-' * 15)
print(f'Voce inseriu os valores: {values}')
print('-=-' * 15)