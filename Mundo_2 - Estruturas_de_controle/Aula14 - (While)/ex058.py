"""
Desafio 058

Problema: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
          em um número entre 0 e 10. Só que agora o jogador irá tentar
          adivinhar até acertar, mostrando no final a quantidade de
          tentativas usadas

          BÔNUS: A escolha deve ser entre 0 e 100
"""

from random import randint
cont = 1

print('-=-'*19)
print('Vou pensar em um numero entre 0 e 100. Tente adivinhar...')
print('-=-'*19)

machine = randint(0, 100)
player = int(input('Digite a sua escolha: '))

while player != machine:
    cont += 1

    if player > machine:
        print('\033[1;31mMuito alto\033[m')
    else:
        print('\033[1;31mMuito baixo\033[m')

    player = int(input('Tente de novo: '))

print('')
print('\033[1;32mPARABÉNS! Você acertou...\033[m O numéro escolhido era {}'.format(player))
print('Você usou {} tentativas para tentar acertar o número'.format(cont))