numero = 0
lista_numeros = []

for i in range(10):
    numero = int(input("Digite números aqui: "))
    lista_numeros.append(numero)

print(f"Maior número: {max(lista_numeros)}")
print(f"Maior número: {min(lista_numeros)}")

