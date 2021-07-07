"""
Desafio 013

Problema:   Faça um algoritmo que leia o salário de uma funcionário e
            mostre seu novo salário, com 15% de aumento.
"""

sal = float(input('Qual é o seu salário ? R$ '))
new_sal = sal + (sal*15/100)

print('\n'+'-' * 50)
print('Seu antigo salario era de RS{:.2f}'.format(sal))
print('Seu novo salário com 15% de desconto é de R${:.2f}'.format(new_sal))
print('-' * 50)