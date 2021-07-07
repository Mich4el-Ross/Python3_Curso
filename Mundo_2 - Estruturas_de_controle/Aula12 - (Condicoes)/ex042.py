"""
Desafio 042

Problema: Refaça o desafio 035 dos triângulos, acrescentando o
          recurso de mostrar que tipo de triângulo será formado:
          - EQUILÁTERO: todos os lados iguais
          - ISÓSCELES: dois lados iguais, um diferente
          - ESCALENO: todos os lados diferentes
"""

print('-=-'*12)
print('{:^36}'.format('Analisador de triangulos'))
print('-=-'*12)

print('')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

print('')

if a < b + c and b < a + c and c < a + b:
    print('É POSSÍVEL formar um triangulo ', end='')
    if a == b == c:
        print('QUADRILÁTERO')
    elif a == b or a == c or b == c:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('NÃO É POSSÍVEL formar um triângulo')