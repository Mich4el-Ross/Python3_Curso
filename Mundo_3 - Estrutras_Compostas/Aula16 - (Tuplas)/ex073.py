"""
Desafio 073

Problema: Crie uma tupla preenchida com os 20 primeiros colocados da
          tabela do Brasileirão na ordem de colocação. No final do
          programa, mostre:

            - Uma lista com os times e sua posição
            - Apenas mostre os 5 primeiros colocados
            - Os últimos 4 colocados da tabela
            - Em que posição da tabela está o time do Palmeiras
"""

teams = ( 'Internacional', 'São Paulo', 'Atlético-MG', 'Flamengo',
         'Palmeiras', 'Grêmio', 'Fluminense', 'Santos', 'Corinthians',
         'Bragantino', 'Athletico-PR', 'Ceará SC', 'Atlético-GO', 'Sport',
         'Bahia', 'Vasco', 'Fortaleza', 'Coritiba', 'Goiás', 'Botafofo')

print('-=-' * 13)
print(f'{"Lista dos times do Brasileirão 2020" :^39}')
print('-=-' * 13)

for pos, tim in enumerate(teams):
    print(f'{pos +1 :2} - {tim}')

print('\n' + '-=-' * 15)
print(f'{"DADOS DO BRASILEIRÃO" :^45}')
print('-=-' * 15)

print('\n' + '---' * 10)
print(f'{"Os cinco primeiros são" :^30}\n')
for t in range(0, 5):
    print(f' {t+1} - {teams[t]}')

print('---' * 10)
print(f'{"Os quatro últimos são" :^30}\n')
for t in range(16, 20):
    print(f' {t+1} - {teams[t]}')

print('---' * 10)
print(f'O Palmeiras está na {teams.index("Palmeiras") + 1 }° posição')