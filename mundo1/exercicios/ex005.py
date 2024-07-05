'''
    Exercício 5:
    - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.
'''

# Programa
num = int(input("Digite um número: ")) # Número informado
ant = num -1                           # Antecessor do número informado
suc = num + 1                          # Sucessor do número informado

print("O antecessor de {} é {}".format(num, ant))
print("O sucessor de {} é {}".format(num, suc))