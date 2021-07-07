"""
Desafio 113

Problema: Reencreva a função leiaInt() que fizemos no desafio 104, incluindo agora
          a possibilidade da digitação de um número de tipo inválido.
          Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaInt(msg_1):
    while True:
        try:
            value_1 = int(input(msg_1))
        except (ValueError, TypeError):
            print('\n\033[1;31mERRO: Informe um valor inteiro válido...\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;31mO usuário prefiriu não digitar o número...\033[m')
            return 0
        else:
            return value_1


def leiaFloat(msg_2):
    while True:
        try:
            value_2 = float(input(msg_2))
        except (ValueError, TypeError):
            print('\n\033[1;31mERRO: Informe um valor real válido...\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário prefiriu não digitar o número...\033[m')
            return 0
        else:
            return value_2


n1 = leiaInt('Insira um valor INTEIRO: ')
print()
n2 = leiaFloat('Insira um valor REAL: ')

print(f'\n\033[1;32mO valor inteiro digitado foi {n1} e o real {n2}\033[m')



