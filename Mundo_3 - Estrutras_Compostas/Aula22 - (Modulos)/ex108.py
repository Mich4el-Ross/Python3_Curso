"""
Desafio 108

Problema: Adapte o código do desafio 107, criando uma função adicional chamada moeda()
          que consiga mostrar os valores como um valor monetário formatado.
"""

from ex108_modulo import moeda

value = float(input('Digite o preço: R$ '))
print()

print(f'Aumento de 10% : {moeda.moeda(moeda.aumentar(value, 10))}')
print(f'Redução de 15% : {moeda.moeda(moeda.diminuir(value, 15))}')
print(f'O dobro de {moeda.moeda(value)} temos, {moeda.moeda(moeda.dobro(value))} ')
print(f'A metade de {moeda.moeda(value)} temos, {moeda.moeda(moeda.metade(value))}')