"""
Desafio 031

Problema:       Desenvolva um programa que pergunte a distância de uma viagem em Km.
                Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
                até 200Km e R$0,45 parta viagens mais longas.
"""

print('-=-'*12)
print('{:^36}'.format('Custo para viagens'))
print('até 200 km --> 0,50 por km')
print('acima de 200 km --> 0,45 por km')
print('-=-'*12)

km = int(input('\nInforme a distancia (km) da viagem: '))

if km <= 200:
    print('O custo da viagem será de RS {} reais para {} km '.format(km * 0.50, km))
else:
    print('O custo da viagem para {} km será de R$ {} reais'.format(km, km * 0.45))