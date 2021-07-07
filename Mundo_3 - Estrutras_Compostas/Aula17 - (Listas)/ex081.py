"""
Desafio 081

Problema: Crie um programa que vai ler vários números e colocar em uma lista.
          Depois disso, mostre:
            - Quantos números foram digitados;
            - A lista de valores ordenada de forma decrescente.
            - Se o valor 5 foi digitado e está ou não na lista.
"""

print('-=-' * 13)
print(f'{"EXTRAINDO DADOS" :^39}')
print('-=-' * 13 + '\n')

numbers = []
while True:

    numbers.append(int(input('Digite um valor: ')))

    opc = str(input('Deseja continuar ? [S/N]: ')).strip().upper()

    while opc not in 'SN':
        opc = str(input('Deseja continuar ? [S/N]: ')).strip().upper()

    print()

    if opc == 'N':
        break

numbers.sort(reverse=True)

print('-=-' * 15)
print(f'Voce digitou {len(numbers)} números')
print(f'Os valores inseridos foram {numbers}')

if 5 in numbers:
    print('O valor 5 foi adicionado')
else:
    print('O valor 5 não foi adicionado')
print('-=-' * 15)