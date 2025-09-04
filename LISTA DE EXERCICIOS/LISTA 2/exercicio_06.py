notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0

valor = int(input("Valor saque (Valores inteiros): "))

if valor > 0:
    notas100 = valor // 100
    valor = valor % 100

    notas50 = valor // 50
    valor = valor % 50

    notas20 = valor // 20
    valor = valor % 20

    notas10 = valor // 10

    if notas100 > 0:
        print(f"{notas100} nota de R$ 100")

    if notas50 > 0:
        print(f"{notas50} nota de R$ 50")

    if notas20 > 0:
        print(f"{notas20} nota de R$ 20")

    if notas10 > 0:
        print(f"{notas10} nota de R$ 10")
else:
    print("Digite números positivos, por favor!")