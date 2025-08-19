# Divisei por 4 ou 400
ano = int(input("Ano: "))

if (ano%4 == 0 and ano%100 != 0) or ano%400 == 0:
    print("Esse ano é bissexto")
else:
    print("Esse ano não é bissexto")