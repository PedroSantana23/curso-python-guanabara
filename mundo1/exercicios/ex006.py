'''
    Exercício 6:
    - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
'''

# Programa (Sem a biblioteca math)
num = int(input("Digite um número: ")) # Número informado
dobro = num * 2                        # Dobro do número informado
triplo = num * 3                       # Triplo do número informado
raiz_quadrada = num ** (1/2)           # Raiz quadrada do número informado

print("O dobro de {} é {}".format(num, dobro))
print("O triplo de {} é {}".format(num, triplo))
print("A raiz quadrada de {} é {}".format(num, raiz_quadrada))

