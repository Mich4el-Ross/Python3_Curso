"""
Desafio 049

Problema: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário
          escolher, só que dessa vez utilizando o laço for
"""

num = int(input('Digite um numero que deseja saber a tabuada: '))
result = 0

print('\n'+'-=-'*10)
print('{:^30}'.format('TABUADA'))
print('-=-'*10 + '\n')

for y in range(1, 11):
    result = num * y
    print(num, '{} {:2} = {}'.format('X', y, result))