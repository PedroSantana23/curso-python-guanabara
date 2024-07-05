'''
    Exercício 10:
    - Crie um programa que leia quanto deinheiro uma pessoa tem na carteira e mostre.
'''

# Programa
dinheiro = float(input("Quanto de dinheiro você tem na cartiera? R$"))
dolars = dinheiro / 5.46
print("Com {} reais você consegue comprar {:.2f} dólares.".format(dinheiro, dolars))