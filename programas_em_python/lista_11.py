lista_positivos = []
lista_negativos = []

for i in range(8):

    numero = int(input("Números: "))
    
    if numero < 0:
        lista_negativos.append(numero)
    elif numero > 0:
        lista_positivos.append(numero)

print(f"Lista Negativos: {lista_negativos}")

print(f"Lista positivos: {lista_positivos}")
