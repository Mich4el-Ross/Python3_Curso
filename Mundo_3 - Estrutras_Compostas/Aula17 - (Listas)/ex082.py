"""
Desafio 082

Problema: Crie um programa leia vários números e os coloque em uma lista.
          Depois disso, crie duas listas extras que vão conter apenas os
          valores pares e ímpares digitados, respectivamente.
          Ao final, mostre o conteúdo das três listas geradas.
"""

numbers = []
evens = []
odds = []

while True:

    num = int(input('Digite um valor: '))
    numbers.append(num)
    opc = str(input('Deseja continuar ? [S/N]: ')).strip().upper()

    while opc not in 'SN':
        opc = str(input('Deseja continuar ? [S/N]: ')).strip().upper()

    if opc == 'N':
        break
    print()

for v in numbers:
    if v % 2 == 0:
        evens.append(v)
    else:
        odds.append(v)

print('\n' + '-=-' * 15)
print(f'Lista completa é {numbers}')
print(f'Lista de PARES é {evens}')
print(f'Lista de IMPARES é {odds}')
print('-=-' * 15)