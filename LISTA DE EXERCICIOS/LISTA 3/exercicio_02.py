MAIOR_IDADE = 18
maiores_de_idade = 0
#lista_idade = []

for i in range(20):

    idade = int(input("Idade: "))

    if idade >= MAIOR_IDADE:
        maiores_de_idade += 1
        #lista_idade.append(idade)

print(f"Existe {maiores_de_idade} pessoas maiores de idade!")
#print(f"{lista_idade}")

