"""
Desafio 108

Problema: Adapte o código do desafio 107, criando uma função adicional chamada moeda()
          que consiga mostrar os valores como um valor monetário formatado.
"""


def moeda(num, symb='R$'):
    return f"{symb} {num:.2f}".replace('.', ',')


def aumentar(num=0, adc=0):
    return num + (num * adc)/100


def diminuir(num=0, adc=0):
    return num - (num * adc)/100


def dobro(num=0):
    return num * 2


def metade(num=0):
    return num / 2