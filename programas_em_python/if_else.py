numero = int(input("Número: "))
NUMERO_FIXO = 10

if numero > NUMERO_FIXO:
    print(f"{numero} é maior que {NUMERO_FIXO}")
elif numero == NUMERO_FIXO:
    print(f"{numero} é igual a {NUMERO_FIXO}")
else:
    print(f"{numero} é menor que {NUMERO_FIXO}")
    