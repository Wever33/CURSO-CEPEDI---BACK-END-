sexo = input("Sexo: ").upper()
peso_mulheres = 0
peso_homens = 0

if sexo == "F":
    altura = float(input("Digite a altura: "))
    peso_mulheres = (62.1*altura) -44.7
    print(f"Peso M: {peso_mulheres}")
elif sexo == "M":
    altura = float(input("Digite a altura: "))
    peso_homens = (72.7 * altura) - 58
    print(f"Peso H: {peso_homens}")
else:
    print("Digite apenas F ou M")