"""
Desafio 034

Problema:   Escreva um programa que pergunte o salário de um funcionário e calcule o
            valor do seu aumento. Para salários superiores a R$1250,00, calcule um
            aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

sal = float(input('Digite seu salário atual : R$ '))

if sal <= 1250:
    sal = sal*1.15
else:
    sal = sal * 1.10

print('Seu novo salário é de RS {:.2f}'.format(sal))
