"""
Desafio 026

Problema:   Faça um programa que leia uma frase pelo teclado
            e mostre:
                - Quantas vezes aparece a letra ‘A’;
                - Em que posição ela aparece a primeira vez;
                - Em que posição ela aparece a última vez.
"""

phrase = str(input('Insira uma frase qualquer: ')).strip().upper()

print('Temos {} letras A nessa frase'.format(phrase.count('A')))
print('A primeira letra A se encontra na posição: {}'.format(phrase.find('A') + 1))
print('A ultima letra A se encontra na posiçao: {}'.format(phrase.rfind('A') + 1 ))