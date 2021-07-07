"""
Desafio 070

Problema: Crie um programa que leia o nome e o preço de vários produtos.
          O programa deverá perguntar se o usuário deseja continuar.
          No final, mostre:
            - Quantos prudtos foram comprados;
            - Qual é o total gasto na compra;
            - Quantos produtos custam mais de R$1000;
            - Qual é o nome do produto mais barato.
"""

print('-=-=-=-=-= MERCADINHO -=-=-=-=-=')

total = cont = cont1000 = price_cheap = 0
name_cheap = ''

while True:
    name = str(input('Nome: ')).strip()
    price = float(input('Preço: R$ '))

    total += price
    cont += 1

    if price >= 1000:
        cont1000 += 1

    if cont == 1:
        price_cheap = price
    else:
        if price <= price_cheap:
            name_cheap = name
            price_cheap = price

    opc = ' '
    while opc not in 'NS':
        opc = str(input('Deseja continuar [S/N]: ')).upper().strip()

    print('-=-' * 11)

    if opc == 'N':
        break

print('\n' + '-=-' * 16)
print('Foram registrados {} produtos'.format(cont))
print('O total da compra foi de R$ {}'.format(total))
print('Temos {}  produtos custando mais de R1000.00'.format(cont1000))
print('O produto mais barato foi {} custando {:.2f}'.format(name_cheap, price_cheap))
print('-=-' * 16)