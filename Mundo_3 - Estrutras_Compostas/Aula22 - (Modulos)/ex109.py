"""
Desafio 109

Problema: Modifique as funções que foram criadas no desafio 107 para que elas
          aceitem um paràmetro a mais, informando se o valor retornado por elas
          vai ou não ser formatado pela função moeda(), desenvolvida na aula 108.
"""

from ex109_modulo import moeda

value = float(input('Digite o preço: R$ '))
print()

print(f'Aumento de 10% : {moeda.aumentar(value, 10, True)}')
print(f'Redução de 15% : {moeda.diminuir(value, 15, True)}')
print(f'O dobro de {moeda.moeda(value)} temos, {moeda.dobro(value, True)}')
print(f'A metade de {moeda.moeda(value)} temos, {moeda.metade(value, True)}')