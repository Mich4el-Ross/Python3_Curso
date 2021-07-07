"""
Desafio 076

Problema: Desenvolva um programa que leia quatro valores pelo teclado
          e guarde-os em uma tupla.
          No final, mostre:

            - Quantas vezes apareceu o valor 9;
            - Em que posição foi digitado o primeiro valor 3;
            - Quais foram os números pares.
"""

shop_list = ('TV', 1800, 'X-box', 1500, 'Playstation 4', 2500, 'Cadeira Gamer', 350,
             'Computador', 2399, 'Celular', 1780, 'Impressora', 1050, 'Teclado', 100,
             'Echo Dot', 499, 'Smart Watch', 235)


print('-=-' * 15)
print(f'{"ELETRONICS MD" :^45}')
print('-=-' * 15 + '\n')

for x in range(0, len(shop_list)):
    if x % 2 == 0:
        print(f'{shop_list[x] :.<30}', end='')
    else:
        print(f' R$ {shop_list[x] :>8.2f}')