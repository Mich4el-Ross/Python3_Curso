"""
Desafio 040

Problema: Crie um programa que leia duas notas de um aluno e calcule
          sua média, mostrando uma mensagem no final, de acordo com a
          média atingida?
          - Média abaixo de 5.0: REPROVADO
          - Média entre 5.0 e 6.9: RECUPERAÇÃO
          - Média 7.0 ou superior: APROVADO
"""

num_1 = float(input('Insira a sua primeira nota obtida: '))
num_2 = float(input('Insira a sua segunda nota obtida: '))
average = (num_1 + num_2) / 2
print('')

print('-=-'*13)
print('Sua média foi {:.2f}'.format(average))

if average >= 7:
    print('PARABÉNS! Você foi APROVADO')
elif average < 5:
    print('Você está REPROVADO')
else:
    print('Você está de RECUPERAÇÃO')

print('-=-'*13)