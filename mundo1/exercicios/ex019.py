'''
    Exercício 19:
    - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.      
'''

# Programa
from random import choice

aluno1 = str(input("Primeiro Aluno: "))
aluno2 = str(input("Segundo Aluno: "))
aluno3 = str(input("Terceiro Aluno: "))
aluno4 = str(input("Quarto Aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = choice(lista)

print("O aluno escolhisdo foi {}".format(escolhido))