'''
    Exercício 8:
    - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

# Programa
medida = float(input("Digite uma medida em metros: ")) # Número informado
km = medida / 1000                                     # Conversão para quilômetros
hm = medida / 100                                      
dam = medida / 10
dm = medida * 10
cen = medida * 100
mil = medida * 1000

print("{} m equivale a {} km".format(medida, km))
print("{} m equivale a {} hm".format(medida, hm))
print("{} m equivale a {} dam".format(medida, dam))
print("{} m equivale a {} dm".format(medida, dm))
print("{} m equivale a {} cm".format(medida, cen))
print("{} m equivale a {} mm".format(medida, mil))