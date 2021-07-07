"""
Desafio 109

Problema: Modifique as funções que foram criadas no desafio 107 para que elas
          aceitem um paràmetro a mais, informando se o valor retornado por elas
          vai ou não ser formatado pela função moeda(), desenvolvida na aula 108.
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