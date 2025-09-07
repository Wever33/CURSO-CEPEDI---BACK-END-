lista_1 = []
lista_2 = []
lista_composta = []
numeros = 0

for i in range(10):
    numeros = int(input("Digite números aqui: "))
    lista_1.append(numeros)

print("\n---------------SEGUNDA LISTA------------------\n")

for ii in range(10):
    numeros = int(input("Digite números aqui: "))
    lista_2.append(numeros)

lista_composta.extend(lista_1)
lista_composta.extend(lista_2)

print(f"\nLISTA 1 : {lista_1}")
print(f"LISTA 2 : {lista_2}")
print(f"LISTA COMPOSTA: {lista_composta}")