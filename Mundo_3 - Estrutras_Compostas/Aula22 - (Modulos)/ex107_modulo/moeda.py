"""
Desafio 107

Problema: Crie um módulo chamado moedas.py que tenha as funções incorporadas
          aumentar(), diminuir(), dobro() e metade().

          Faça também um programa que importe esse módulo e use algumas dessas
          funçóes.
"""


def aumentar(num, adc):
    return num + (num * adc)/100


def diminuir(num, adc):
    return num - (num * adc)/100


def dobro(num):
    return num * 2


def metade(num):
    return num / 2