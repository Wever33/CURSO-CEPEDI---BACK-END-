mensagem = """
    Escolha umas das opções:

    SOMAR = [+]
    MULTIPLICAÇÃO = [*]
    DIVISIÃO = [/]
    DIVISÃO INTEIRA = [//]
    RESTO = [%]
    EXPONENCIAÇÃO = [**]
"""
     
opcao = input(mensagem)

operacao = 0

if opcao == "+":
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))
    operacao = numero_1 + numero_2
    print(f"{numero_1} {opcao} {numero_2} = {operacao}")
    
elif opcao == "*":
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))
    operacao = numero_1 * numero_2
    print(f"{numero_1} {opcao} {numero_2} = {operacao}")

elif opcao == "/":
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))
    operacao = numero_1 / numero_2
    print(f"{numero_1} {opcao} {numero_2} = {operacao}")

elif opcao == "//":
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))
    operacao = numero_1 // numero_2
    print(f"{numero_1} {opcao} {numero_2} = {operacao}")

elif opcao == "%":
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))
    operacao = numero_1 % numero_2
    print(f"{numero_1} {opcao} {numero_2} = {operacao}")

elif opcao == "/":
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))
    operacao = numero_1 ** numero_2
    print(f"{numero_1} {opcao} {numero_2} = {operacao}")

else:
    print("Operação inválida")