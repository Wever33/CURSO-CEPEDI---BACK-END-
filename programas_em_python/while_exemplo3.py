soma_idade = 0
idade = 0
#opcao = "S"
contador = 0

while True:
    idade = int(input("Digite sua idade: "))
    soma_idade += idade
    contador += 1
    opcao = input("Deseja continuar? Sim - [S] ou Não - [N]: ").upper()
    if opcao == "N":
        break

print("Soma das idades: ", soma_idade/contador)