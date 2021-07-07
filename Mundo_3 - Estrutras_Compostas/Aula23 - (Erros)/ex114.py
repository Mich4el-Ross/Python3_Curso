"""
Desafio 114

Problema: Crie um código em Python que teste se um site de sua preferência
          está acessível pelo computador usado.
"""

import urllib
import urllib.request
from datetime import datetime

time = datetime.today()
data_hora = time.strftime('%d/%m/%Y %H:%M')

try:
    site = urllib.request.urlopen('https://www.google.com.br/')
except urllib.error.URLError:
    print('\33[1;31m-=-' * 20 + f'\n{"A CONEXÃO FOI PERDIDA :(":^60}\n' + '-=-' * 20 + '\33[m')
    print(f'\n\33[1mO site não está acessível, última tentativa em {data_hora}\33[m')
else:
    print('\33[1;32m-=-' * 20 + f'\n{"CONEXÃO REALIZADA COM SUCESSO :)":^60}\n' + '-=-' * 20 + '\33[m')
    print(f'\n\33[1mAcesso à: https://www.google.com.br/ as {data_hora}\33[m')



