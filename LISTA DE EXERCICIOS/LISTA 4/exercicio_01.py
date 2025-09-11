lista_pares = []
lista_impares = []
lista_numeros = []
numeros = 0

for i in range(2):

    numeros = int(input("Digite números aqui: "))
    lista_numeros.append(numeros)

    if numeros % 2 == 0:
        lista_pares.append(numeros)
    
    else:
        lista_impares.append(numeros)

print("\n----------------------------------------")
print(f"\n Lista números: {lista_numeros}")
print(f"\n Lista números PARES: {lista_pares}")
print(f"\n Lista números ÍMPARES: {lista_impares}")
print("\n----------------------------------------")