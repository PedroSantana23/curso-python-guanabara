'''
    Exercício 7:
    - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''

# Programa

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

print("A média do aluno foi de {:.2f}".format(media))