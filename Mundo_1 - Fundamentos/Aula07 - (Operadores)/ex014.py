"""
Desafio 014

Problema:   Escreva um programa que converta um a temperatura digitada
            em ºC e converta para ºF
"""

celsius = float(input('Informe a temperatura em °C:'))
fahrenheit = ((9 * celsius) / 5) + 32

print('O valor de {}°C equivale a {}°F '.format(celsius, fahrenheit))