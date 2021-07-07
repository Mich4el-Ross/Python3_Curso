"""
Desafio 102

Problema: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:

            - o primeiro que indique o número a calcular;
            - e o outro chamado show;

          O show será um valor lógico opcional indicando se será mostrado ou não na tela
          o processo de cálculo do fatorial.
"""


def fatorial(number, show=False):
    """
    :param number: O número a ser calculado
    :param show: Valor opcional que mostra ou não a conta
    :return: O valor da conta
    """

    fat = 1
    for c in range(number, 0, -1):
        fat *= c
        if show:
            print(c, end=' X ' if c != 1 else ' = ')
    return fat

print('-=-' * 7 + '\n Cálculo de Fatorial \n' + '-=-' * 7)

print(fatorial(5))              # Somente o resultado é mostrado
print()
print(fatorial(7, show=True))   # Conta com o resultado
print()
help(fatorial)                  # Explicação da função
