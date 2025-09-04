menu = """

 [+] = SOMA
 [-] = SUBTRAÇÃO
 [*] = MULTIPLICAÇÃO
 [/] = DIVISÃO   

"""
opcao = input(menu)
calculo = 0

if opcao == "+":
        numero1, numero2 = float(input("Primeiro número: ")), float(input("Segundo número: "))
        calculo = numero1 + numero2
        print(f" {numero1} + {numero2} = {calculo}")

if opcao == "-":
        numero1, numero2 = float(input("Primeiro número: ")), float(input("Segundo número: "))
        calculo = numero1 - numero2
        print(f" {numero1} - {numero2} = {calculo}")

if opcao == "*":
        numero1, numero2 = float(input("Primeiro número: ")), float(input("Segundo número: "))
        calculo = numero1 * numero2
        print(f" {numero1} x {numero2} = {calculo}")

if opcao == "/":
        numero1, numero2 = float(input("Primeiro número: ")), float(input("Segundo número: "))
        calculo = numero1 / numero2
        print(f"{numero1}\n/\n{numero2} = {calculo}")

     