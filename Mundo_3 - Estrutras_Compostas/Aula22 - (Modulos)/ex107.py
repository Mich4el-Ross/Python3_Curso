"""
Desafio 107

Problema: Crie um módulo chamado moedas.py que tenha as funções incorporadas
          aumentar(), diminuir(), dobro() e metade().

          Faça também um programa que importe esse módulo e use algumas dessas
          funçóes.
"""

from ex107_modulo import moeda


value = float(input('Digite o preço: R$ '))
print()

print(f'Aumento de 10%: {moeda.aumentar(value, 10)}')
print(f'Redução de 15%: {moeda.diminuir(value, 15)}')
print(f'O dobro de {value:.2f} temos, {moeda.dobro(value)} ')
print(f'A metade de {value:.2f} temos, {moeda.metade(value)}')