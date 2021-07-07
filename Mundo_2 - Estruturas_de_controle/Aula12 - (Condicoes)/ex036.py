"""
Desafio 036

Problema: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
          Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
          A prestação mensal não pode exceder 30% do salário ou então o empréstimo será
          negado.
"""

home = float(input('Informe o valor da casa: R$ '))
sal = float(input('Digite seu salário: R$ '))
year = int(input('Informe por quantos anos deseja financiar: '))
month = home / (year*12)
percentage = (sal * 30) / 100

print('\nPara um emprestimo de R$ {:.2f} a {} anos de financiamento, a parcela será de {:.2f}'.format(home, year, month))

if month <= percentage:
    print('Empréstimo \033[1;32m CONCEBIDO \033[m')
else:
    print('Empréstimo \033[1;31m NEGADO \033[m')