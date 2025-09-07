numeros_reais = 0
lista_reais = []

while True:
    numeros_reais = float(input("Digite números reais: "))

    lista_reais.append(numeros_reais)

    if numeros_reais == 0:
        break


print(f"\nMaior número: {max(lista_reais)}")
print(f"\nLista dos números REAIS: {lista_reais}")