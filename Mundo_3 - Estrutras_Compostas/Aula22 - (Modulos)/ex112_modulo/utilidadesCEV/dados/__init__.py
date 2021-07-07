"""
Desafio 112

Problema: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um
          módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja
          capaz de funcionar como a função input(), mas com uma validação de dados
          para aceitar apenas valores que sejam monetários.
"""

def leiaDinheiro(msg):
    valido = False

    while not valido:
        number = str(input(msg)).strip().replace(',', '.')
        if number.isalpha() or number == '':
            print(f'\033[1;31mERRO: "{number}" é um preço invalido!\033[m')
        else:
            valido = True
            return float(number)