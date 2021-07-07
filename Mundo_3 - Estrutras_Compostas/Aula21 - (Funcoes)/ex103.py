"""
Desafio 103

Problema: Faça um programa que tenha uma função chamada ficha(), que receba
          dois parâmetros opcionais: o nome de um jogador e quantos gols ele
          marcou.

          O programa deverá ser capaz de mostrar a ficha do jogador, mesmo
          que algum dado não tenha sido informado corretamente.
"""


def ficha(name='<desconhecido>', goals=0):
    print(f'O jogador {name} fez {goals} gol(s) no campeonato')


player = str(input('Nome do jogador: ')).strip()
score = str(input('Número de gols: ')).strip()

score = int(score) if score.isnumeric() else 0
ficha(goals=score) if player == '' else ficha(player, score)

