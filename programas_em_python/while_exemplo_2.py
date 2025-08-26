soma_numeros = 0
numero = 0


while numero >= 0:
    numero = int(input("Digite numeros inteiros: "))
    
    if numero < 0: break
    soma_numeros += numero


print(f"Soma dos números: {soma_numeros}")
print("Programa encerrado")