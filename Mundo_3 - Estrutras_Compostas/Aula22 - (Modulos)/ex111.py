"""
Desafio 111

Problema: Crie um pacote chamado utilidadesCEV que tenha dois módulos internos chamados
          moeda e dado.
          Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para
          o primeiro pacote e mantenha tudo funcionando.
"""

from ex111_modulo.utilidadesCEV import moeda

value = float(input('Digite o preço: R$ '))
print()

moeda.resumo(value, 75, 20)