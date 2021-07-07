"""
Desafio 105

Problema: Faça um programa que tenha uma função chamada notas() que pode receber
          várias notas de alunos e vai retornar um dicionário com as seguintes
          informações:

            - Quantidade de notas
            - A maior nota
            - A menor nota
            - A média da turma
            - A situação (opcional)
"""

def notas(*values, sit=False):

    final = dict()
    final['Total'] = len(values)
    final['Menor nota'] = min(values)
    final['Maior nota'] = max(values)
    final['Média'] = sum(values) / len(values)

    if sit:
        if final['Média'] >= 7:
            final['Situação'] = 'Muito boa'
        elif 7 > final['Média'] > 5:
            final['Situação'] = 'Razoável'
        else:
            final['Situação'] = 'Péssima'

    return final


report = notas(8.5, 9.5, 6.5, 7.5, sit=True)
print()
print(report)


