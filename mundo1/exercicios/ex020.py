'''
    Exercício 20:
    - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
'''

# Programa
from random import shuffle

aluno1 = str(input("Primeiro Aluno: "))
aluno2 = str(input("Segundo Aluno: "))
aluno3 = str(input("Terceiro Aluno: "))
aluno4 = str(input("Quarto Aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print("A ordem da apresentação será: ")
print(lista)

