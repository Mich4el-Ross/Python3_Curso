"""
Desafio 111

Problema: Crie um pacote chamado utilidadesCEV que tenha dois módulos internos chamados
          moeda e dado.
          Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para
          o primeiro pacote e mantenha tudo funcionando.
"""


def moeda(num, symb='R$'):
    return f"{symb} {num:.2f}".replace('.', ',')


def aumentar(num=0, adc=0, form=False):
    if form:
        return moeda(num + (num * adc)/100)
    else:
        return num + (num * adc)/100


def diminuir(num=0, adc=0, form=False):
    if form:
        return moeda(num - (num * adc)/100)
    else:
        return num - (num * adc)/100


def dobro(num=0, form=False):
    if form:
        return moeda(num * 2)
    else:
        return num * 2


def metade(num=0, form=False):
    if form:
        return moeda(num / 2)
    else:
        return num / 2


def resumo(num=0, aum=0, dim=0):
    print('-=-' * 11 + f'\n{"RESUMO DO VALOR":^33}\n' + '-=-' * 11)

    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{aum}% de aumento: \t{aumentar(num, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(num, dim, True)}')

    print('-=-' * 11)