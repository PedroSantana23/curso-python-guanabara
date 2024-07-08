'''
    Exercício 18:
    - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

# Programa 
from math import sin, cos, tan
ang = float(input("Digite o ângulo: "))
seno = sin(ang)
cosseno = cos(ang)
tangente = tan(ang)

print("Ângulo = {}".format(ang))
print("Seno de {} é igual a {}".format(ang, seno))
print("Cosseno de {} é igual {}".format(ang, cosseno))
print("Tangente de {} é igual {}".format(ang, tangente))
