"""
Desafio 044

Problema: Elabore um programa que calcule o valor a ser pago
          por um produto, considerando o seu preço normal e
          condição de pagamento:
          - à vista dinheiro/cheque: 10% de desconto
          - à vista no cartão: 5% de desconto
          - em até 2x no cartão: preço normal
          - 3x ou mais no cartão: 20% de juros

"""

product = float(input('Insira o valor do item a ser comprado: R$ '))
print('')

print('-=-'*11)
print('{:^33}'.format('OPÇOES DE PAGAMENTO'))
print('[1] --> Dinheiro / Cheque')
print('[2] --> Cartão')
print('[3] --> 2x no cartão')
print('[4] --> 3x ou mais no cartão')
print('-=-'*11)
opc = int(input('Sua opção: '))

print('')

if opc == 1:
    price = product * (90/100)
    print('Sua compra vai custar R$ {:.2f}'.format(price))
elif opc == 2:
    price = product * (95/100)
    print('Sua compra vai custar R$ {:.2f}'.format(price))
elif opc == 3:
    print('Sua compra vai custar R$ {}'.format(product))
elif opc == 4:
    price = product * 1.20
    print('Sua compra vai custar R$ {:.2f}'.format(price))
else:
    print('Selecione uma opção válida!')
