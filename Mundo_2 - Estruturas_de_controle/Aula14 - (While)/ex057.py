"""
Desafio 057

Problema: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
          'M' ou 'F'. Caso esteja errado peça a digitaçao novamente até ter um valor
          correto
"""

genre = str(input('Digite seu sexo [M/F]: ')).strip().upper()

while genre not in 'MF':
    genre = str(input('Dados Inválidos. Por favor, insira seu sexo: ')).strip().upper()

print('\n' + '-=-'*18)
if genre == 'M':
    print('Pessoa do sexo masculino (M) cadastrada com sucesso')
if genre == 'F':
    print('Pessoa do sexo feminino (F) cadastrada com sucesso')
print('-=-'*18)