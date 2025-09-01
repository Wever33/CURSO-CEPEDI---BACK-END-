mensagem = ""

lista_dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
quantidade = len(lista_dias)

for i in range(quantidade):

    opcao_numero = int(input("Escolha um números de 1 até 7: "))

    for indice, dia in enumerate(lista_dias):
        #print(f"{dia} = {indice+1}")

        if opcao_numero == indice+1:
            print(f"Parabéns, você descobriu {dia} = {indice+1}")
            mensagem += f"""
    [{indice+1}] - {dia.upper()}
    """     

print("\n--------- DIAS DESCOBERTOS ---------")
print(mensagem)
    


