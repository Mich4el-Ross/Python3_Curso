"""
Desafio 101

Problema: Crie um programa que tenha uma função chamada voto() que vai receber
          como parâmetro o ano de nascimento de uma pessoa, retornando um valor
          literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO.
"""


def voto (value):

    from datetime import date
    year = date.today().year
    age = year - value

    if age < 16:
        return f'\nCom {age} anos você NÃO VOTA!'
    if 18 <= age <= 65:
        return f'\nCom {age} anos você É OBRIGADO A VOTAR!'
    else:
        return f'\nCom {age} anos o VOTO É OPCIONAL!'


born_date = int(input('Digite sua data de nascimento:'))
print(voto(born_date))