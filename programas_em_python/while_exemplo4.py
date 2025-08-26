numero = int(input("Digite uma número: "))

while numero != 0:
    if numero%2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é impar")
    numero = int(input("Digite números aqui: "))