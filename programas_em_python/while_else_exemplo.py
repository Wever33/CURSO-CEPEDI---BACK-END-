numero = int(input("Digite números: "))
cont = 0
i = 2

while i < numero:
    r = numero % i
    i += 1
    if r == 0:
        cont += 1

if cont == 0:
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")

