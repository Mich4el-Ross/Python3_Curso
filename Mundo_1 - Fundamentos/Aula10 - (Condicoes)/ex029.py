"""
Desafio 029

Problema:       Escreva um programa que leia a velocidade de um carro. Se ele
                ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi
                multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

print('-=-'*10)
print('{:^30}'.format('Verificação de Trânsito'))
print('-=-'*10)

vel = float(input('\nQual a velocidade do seu carro (km/h): '))

if vel>80:
    mult = 7 * (vel-80)
    print('Você foi MULTADO por exceder o limite de velocidade que é 80km/h')
    print('A multa é de R$ {} reais'.format(mult))
else:
    print('Tenha um bom dia...Você respeitou o limite')