'''
    Exercício 14:
    - Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''

# Programa
celsius = float(input("Temperatura em Graus Celsius: "))
fahrenheit = 1.8*celsius + 32
print("A temperatura {} Celsius convertida para Fahrenheit fica {:.1f} F".format(celsius, fahrenheit))