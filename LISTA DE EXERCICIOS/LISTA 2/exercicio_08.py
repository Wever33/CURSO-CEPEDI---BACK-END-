lista_de_perguntas = ["Telefonou para a vítima no último mês?", "Esteve no local do crime na última semana?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
resposta = ""
lista_de_resposta = []
respostas_positivas = 0

for numero_da_pergunta, pergunta in enumerate(lista_de_perguntas):

    print(f"\nPergunta {numero_da_pergunta+1}: {pergunta} ")
    resposta = input("\nResposta: Digite [Sim ou Não]: ").lower()
    lista_de_resposta.append(resposta)

respostas_positivas = lista_de_resposta.count("sim")

if respostas_positivas == 2:
    print("\nStatus: Inocente, porém Suspeito(a!")

elif respostas_positivas == 3 or respostas_positivas == 4:
    print("\nStatus: Cúmplice!")

elif respostas_positivas == 5:
    print("\nStatus: Assasino!")
    
else:
    print("\nStatus: Nenhuma suspeita!")

    