"""
Desafio 104

Problema: Crie um programa que tenha a função leiaint(), que vai funcionar de forma
          semelhante a função input(), só que fazendo a validação para aceitar apenas
          um valor númerico.

          Ex:
            n = leiaint('Digite um n: ')
"""


def leiaInt(msg):
    value = input(msg).strip()

    while not value.isnumeric():
        print('\33[1;31mERRO! Informe um valor inteiro...\33[m')
        value = input(msg).strip()

    return value


number = leiaInt('Digite um número: ')
print(f'\nVocê digitou o número {number}')