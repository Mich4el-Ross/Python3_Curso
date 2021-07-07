"""
Desafio 043

Problema: Desenvolva um programa que leia o peso e a altura de
          uma pessoa, calcule seu Índice de Massa Corporal (IMC)
          e mostre seu status, de acordo com a tabela abaixo:
            - IMC abaixo de 18,5: Abaixo do Peso
            - Entre 18,5 e 25: Peso Ideal
            - 25 até 30: Sobrepeso
            - 30 até 40: Obesidade
            - Acima de 40: Obesidade Mórbida
"""

weight = float(input('Insira seu peso (Kg): '))
height = float(input('Insira sua altura (m): '))
IMC = weight / (height ** 2)

print('')

print('Seu IMC é de {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está na categoria: ABAIXO DO PESO')
elif IMC < 25:
    print('Você está na categoria: PESO IDEAL')
elif IMC < 30:
    print('Você está na categoria: SOBREPESO')
elif IMC < 40:
    print('Você está na categoria: OBESIDADE')
else:
    print('Você está na categoria: OBESIDADE MÓRBIDA')