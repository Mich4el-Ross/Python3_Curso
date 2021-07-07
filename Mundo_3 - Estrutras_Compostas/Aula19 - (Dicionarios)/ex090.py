"""
Desafio 090

Problema:   Faça um programa que leia o nome e média de um aluno, guardando também a situação
            em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""

student = {}

student['Nome'] = str(input('Nome: '))
student['Média'] = float(input(f'Média de {student["Nome"]}: '))

if student['Média'] >= 7:
    student['Situação'] = 'Aprovado'
elif student['Média'] >= 5:
    student['Situação'] = 'Recuperação'
else:
    student['Situação'] = 'Reprovado'

print('\n' + '-=-' * 10)
for k, v in student.items():
    print(f'{k} é igual a {v}.')
print('-=-' * 10)
