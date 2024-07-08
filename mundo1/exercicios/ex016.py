'''
    Exercício 16:
    - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
    Ex: Digite um número: 6.127
    O número 6.127 tem a parte inteira 6.
'''

# Programa (Sem a lib Math)
num = float(input("Digite um número: "))
porcao_inteira = num // 1
print("O número {} tema parte inteira {}".format(num, porcao_inteira))