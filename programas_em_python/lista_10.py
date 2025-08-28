quantidade_numeros = int(input("Quantidade de números: "))

lista = []
numero = 0

for i in range(quantidade_numeros):
    numero = int(input("Números: "))
    lista.append(numero)

print("-----------------------------")

for ii in reversed (lista): # Forma de reverse
    print(ii)