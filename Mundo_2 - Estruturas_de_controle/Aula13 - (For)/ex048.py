"""
Desafio 048

Problema: Crie um progrma que calcule a soma entre todos os números impares
          que são multiplos de 3 e que se encontram no intervalo de 1 até 500
"""

sum = 0
mul = 0

for x in range(3, 501, 3):
    if x % 2 == 1:
        sum += x
        mul += 1
print('Temos {} multiplos ímpares de 3 entre 1 e 500 '.format(mul))
print('A soma entre esses multiplos é {}'.format(sum))