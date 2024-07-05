'''
    Exercício 4:
    - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

# Programa

text = input("Digite algo: ")
print('O tipo primitivo do valor informado é {}'.format(type(text))) # Tipo primitivo da variável
print('Só tem espaços? {}'.format(text.isspace()))                   # Verifica se só tem espaços
print('É um número? {}'.format(text.isnumeric()))                    # Verifica se é um número
print('É alfabético? {}'.format(text.isalpha()))                     # Verifica se é alfabético 
print('É alfanumérico? {}'.format(text.isalnum()))                   # Verifica se é alfanumérico
print('Está em maiúsculas? {}'.format(text.isupper()))               # Verifica se tem letra maiúscula
print('Está em minúsculas? {}'.format(text.islower()))               # Verifica se tem letra minúscula
print('Está capitalizada? {}'.format(text.istitle()))                # Verifica se é um título