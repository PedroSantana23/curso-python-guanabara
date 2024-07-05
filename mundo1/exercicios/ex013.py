'''
    Exercício 13:
    - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

# Programa

salario = float(input("Informe o salário do funcionário(a): "))
salario_aumento = salario + salario*15/100
print("O funcionário que recebe R$ {}, com aumento de 15%, vai passar a ganhar R$ {:.2f}".format(salario, salario_aumento))