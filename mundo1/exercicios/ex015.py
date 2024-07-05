'''
    Exercício 15:
    - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

# Programa 
km_percorrido = float(input("Quilômetros rodados: "))
quant_dias = int(input("Total de dias que o carro foi alugado: "))
preco = (quant_dias*60) + (km_percorrido*0.15)
print("Preço: R$ {:.2f}".format(preco))