"""
Desafio 032

Problema:   Faça um programa que leia um ano qualquer e mostre se
            ele é bissexto ou não.
"""

import datetime

year = int(input('Digite um ano para ser analisado (yyyy) ou digite [0] para  o ano atual:'))

if year == 0:
    year = datetime.datetime.now().year

if year % 4 == 0 and year % 100 != 0 or year == 0:
    print('O ano de {} é bissexto'.format(year))
else:
    print('O ano de {} não é bissexto'.format(year))