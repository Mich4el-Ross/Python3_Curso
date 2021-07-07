"""
Desafio 106

Problema: Faça um mini-sistema que utilize o interative Help do Python. O usuário
          vai digitar o comando e o manual vai aparecer. Quando o usuário digitar
          a palavra 'FIM' o programa se encerrará.

          Obs: Use cores.
"""


def ajuda():
    from time import sleep

    while True:
        print('\33[1;34m-=-' * 12 + f'\n{"Sistema INTERACTIVE HELP":^36}\n' + '-=-' * 12 + '\33[m')
        resp = input('\33[1mFunção ou Biblioteca >>> \33[m').strip().lower()

        if resp == "fim":
            print('\n\033[1;31mFinalizando...\033[m')
            sleep(3)
            break

        print('\33[1;37m')
        help(resp)
        print('\33[m')


ajuda()