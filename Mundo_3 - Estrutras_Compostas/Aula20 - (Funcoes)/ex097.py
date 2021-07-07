"""
Desafio 097

Problema: Faça um programa que tenha uma função chamada escreva(), que receba
          um texto qualquer como parâmetro e mostre uma mensagem com o tamanho
          adaptável.
"""


def escreva(msg):
    print((len(msg) + 2) * '-')
    print(msg)
    print((len(msg) + 2) * '-')


escreva(' Olá, Mundo!')
escreva(' Curso de Python 3.0')
escreva(' Minha primeira linguagem de programação')