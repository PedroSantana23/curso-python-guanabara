'''
    Exercício 17:
    - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''

# Programa
from math import hypot
co = float(input("Cateto Oposto: "))
ca = float(input("Cateto Adjacente: "))
hip = hypot(co, ca)
print("Um triângulo com o cateto oposto igual a {} e o cateto adjacente igual a {} tem a hipotenusa igual a {}".format(co, ca, hip))