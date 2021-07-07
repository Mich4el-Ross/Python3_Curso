"""
Desafio 079

Problema: Crie um programa onde o usuário possa digitar vários valores
          númericos e a partir disso cadastre-os em uma lista. Caso o
          número já exista lá dentro, ele não será adicionado. No final,
          serão exibidos os valores únicos digitados, em ordem crescente.
"""

values = []

print('-=-' * 15)
print(f'{"LEITOR DE NÚMEROS" :^45}')
print('-=-' * 15)

while True:
    num = int(input('Digite um valor: '))

    if num in values:
        print('\033[1;31mValor DUPLICADO! Não vou adicionar...\033[m')
    else:
        values.append(num)
        print('\033[1;32mValor adicionado com sucesso...\033[m')

    print()

    opc = str(input('Deseja continuar ? [S/N]: ')).strip().upper()

    while opc not in 'SN':
        opc = str(input('Deseja continuar ? [S/N]: ')).strip().upper()

    if opc in 'N':
        break
    print()

values.sort()

print('\n' + '-=-' * 15)
print(f'Voce inseriu os valores: {values}')
print('-=-' * 15)