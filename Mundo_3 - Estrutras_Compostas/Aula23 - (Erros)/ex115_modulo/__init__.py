def header():
    from time import sleep
    print('\33[1;34m-=-' * 12 + f'\n{"Sistema de Cadastro":^36}\n' + '-=-' * 12 + '\33[m')
    print('\33[1;33m1)\33[m \33[1;30mVer pessoas cadastradas\33[m')
    print('\33[1;33m2)\33[m \33[1;30mCadastrar novas pessoas\33[m')
    print('\33[1;33m3)\33[m \33[1;30mFinalizar o programa\33[m')
    print('\33[1;34m-=-' * 12 + '\33[m')

    try:
        opc = int(input('\33[1;33mSua opção >>>\33[m '))
    except (TypeError, ValueError):
        print('\33[31mERRO: Digite um número inteiro válido...\33[m\n')
        sleep(2)
    else:
        if opc == 1:
            sleep(1.5)
            view()
        elif opc == 2:
            sleep(1.5)
            register()
        elif opc == 3:
            sleep(1.5)
            stop()
        else:
            print('\33[31mERRO: Opção inválida. Tente novamente...\33[m\n')
            sleep(2)


def view():
    from time import sleep

    database = open('ex115_modulo/database.txt', 'r', encoding='utf-8')

    print('\n' + '\33[1;30m-=-' * 12 + f'\n{"Dados Cadastrados":^36}\n' + '-=-' * 12 + '\33[m')
    print(f'\33[30;1m{"NOME":<30}{"IDADE":^6}\n\33[m', end='')

    for line in database.readlines():
        datas = line.split()            # Tratamento dos dados
        name = ' '.join(datas[:-1])     # Separando os nomes
        old = datas[-1]                 # Separando as idades

        print(f'\33[30;1m{name:<30}{old:^6}')

    database.close()

    print('-=-' * 12 + '\33[m\n')
    sleep(1.5)


def register():
    from time import sleep
    data = open('ex115_modulo/database.txt', 'a', encoding='utf-8')
    print('\n' + '\33[1;32m-=-' * 12 + f'\n{"Cadastrar Pessoas":^36}\n' + '-=-' * 12 + '\33[m')

    name = str(input('\33[30;1mInsira o nome: ')).title().strip()
    old = str(input('Insira a idade: \33[m')).strip()

    data.write(f'\n{name} {old}')
    data.close()

    print('\33[1;32m' + '-=-' * 12 + '\33[m')

    sleep(0.5)
    print(f'\33[1;31mPessoa Cadastrada!!\33[m\n')
    sleep(1.5)


def stop():
    from time import sleep
    print()
    print('\33[1;31m-=-' * 12 + f'\n{"Finalizando o programa...":^36}\n' + '-=-' * 12 + '\33[m\n')
    sleep(1.5)
    exit(0)