'''
    Exercício 11:
    - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''

# Programa

larg = float(input("Largura da parede em metros: "))
alt = float(input("Altura da parede em metros: "))
area = larg * alt
litros = area/2
print("A parede tem as dimensões {}x{}".format(larg, alt))
print("Área = {} m2".format(area))
print("Litros = {} litros de tinta".format(litros))
