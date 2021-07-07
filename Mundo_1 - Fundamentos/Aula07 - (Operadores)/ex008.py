"""
Desafio 008

Problema:   Escreva um programa que leia um valor em metros e o
            exiba convertido em centímetros e milímetros.
"""

metros = float(input('Digite a distancia em metros: '))
print('A distancia de {} corresponde a:\n'.format(metros))

dc = metros*10
cm = metros*100
mm = metros*1000
dam = metros/10
hm = metros/100
km = metros/1000

print('{} km '.format(km))
print('{} hm'.format(hm))
print('{} dam'.format(dam))
print('{:.0f} dm'.format(dc))
print('{:.0f} cm'.format(cm))
print('{:.0f} mm'.format(mm))