produtos = []
precos_produtos = []

nome_dos_produtos = ""
preco = 0

NUMEROS_DE_PRODUTOS = 2
contador_preco_50 = 0
produtos_entre_50_e_100 = ""
media_preco = 0
soma_precos = 0
contador_preco_maior_100 = 0

#print("\n---------------------------------------------------------------")
for i in range(NUMEROS_DE_PRODUTOS):

    nome_dos_produtos = input("\nDigite o nome do produto: ")
    preco = float(input(f"\nDigite o preço de {nome_dos_produtos}: "))

    produtos.append(nome_dos_produtos)
    precos_produtos.append(preco)

for preco, nome_dos_produtos in zip(precos_produtos, produtos):

    if preco < 50:
        contador_preco_50 += precos_produtos.count(preco)

    if preco >= 50 and preco <= 100:
        produtos_entre_50_e_100 += f"{nome_dos_produtos}"

    if preco > 100:

        contador_preco_maior_100 += precos_produtos.count(preco)
        soma_precos += preco
        media_preco = soma_precos/contador_preco_maior_100


        

print(contador_preco_50)
print(produtos_entre_50_e_100)
print(media_preco)