"""
Desafio 110

Problema: Adicione ao módulo moeda() criado nos desafios anteriores, uma função
          chamada resumo(). que mostre na tela algumas informações geradas pelas
          funções que já temos no módulo criado até aqui.
"""

from ex110_modulo import moeda

value = float(input('Digite o preço: R$ '))
print()

moeda.resumo(value, 80, 35)
