from math import sqrt

numero = float(input("Número: "))

if numero > 0:
    print(f"A raiz quadrada é: {sqrt(numero):.2f}")
else:
    print("Não é possivel tirar raiz quadrado de número")