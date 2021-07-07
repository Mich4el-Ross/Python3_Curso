"""
Desafio 087

Problema: Aprimore o desafio anterior (86), mostrando no final do programa:
            - A soma dos valores pares digitados;
            - A soma dos valores da terceira coluna;
            - O maior valor da segunda linha

"""

matriz = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
]
evens = third = 0

for r in range(0, 3):
    for c in range(0, 3):
        matriz[r][c] = int(input(f'Insira um valor para [{r}, {c}]: '))

        if matriz[r][c] % 2 == 0:
            evens += matriz[r][c]
        if matriz[r][2]:
            third += matriz[r][2]

print('-=-' * 15)

for r in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[r][c] :^5}]', end=' ')
    print()

print('-=-' * 15)
print(f'A soma dos valores PARES é: {evens}')
print(f'A soma dos valores da terceira coluna é: {third}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
print('-=-' * 15)