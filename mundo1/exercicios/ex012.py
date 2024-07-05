'''
    Exercício 12:
    - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

# Programa 

preco = float(input("Preço: R$"))
desconto = preco - preco*5/100
print("O preço {} do produto fica {:.2f} se descontado 5% de seu valor inicial".format(preco, desconto))
