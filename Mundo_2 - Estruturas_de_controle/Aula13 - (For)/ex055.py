"""
Desafio 055

Problema: Faça um prgrama que leia o peso de cinco pessoas. No final, mostre
          qual foi o maior e o menor peso lidos
"""

lighter = 0
heaviest = 0

for x in range(1, 6):
    weight = float(input('Digite o seu peso (Kg) da {}° pessoa: '.format(x)))
    if x == 1:
        heaviest = weight
        lighter = weight
    else:
        if weight >= heaviest:
            heaviest = weight
        if weight < lighter:
            lighter = weight

print('')
print('A pessoa mais leve que foi cadastrada possui {} Kg'.format(lighter))
print('A pessoa mais pesada que foi cadastrada possui {} Kg'.format(heaviest))