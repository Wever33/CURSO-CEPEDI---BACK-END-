dicionario_pessoas = {}

for i in range(10):

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    print("-----------------")

    dicionario_pessoas [nome] = idade


idade_mais_nova = min(dicionario_pessoas.values())

for nome, idade in dicionario_pessoas.items():

        if idade == idade_mais_nova:
              print(f"A pessoa mais jovem é {nome} com {idade} anos")



