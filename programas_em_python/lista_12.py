
lista_temperatura = []

for i in range(12):

    temperatura = float(input("Temperatura (°C): "))
    lista_temperatura.append(temperatura)

print(f"A maior temperatura: {max(lista_temperatura)} °C")
print(f"A menor temperatura: {min(lista_temperatura)} °C")

