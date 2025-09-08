QUANTIDADE_DE_DIAS = 7
quantidade_de_sacos = 0
quantidade_de_sacos_semana = []
quantidade_de_sacos_limite = []
resto = 0

for i in range(QUANTIDADE_DE_DIAS):
    quantidade_de_sacos = int(input("Quantidade de sacos: "))
    quantidade_de_sacos_semana.append(quantidade_de_sacos)

for dia, sacos in enumerate(quantidade_de_sacos_semana):

    if sacos > 29:
        quantidade_de_sacos_limite.append(f"\n|Dia {dia+1} = {sacos} sacos") 


print(f"\nQuantidade de sacos de cimento usado na semana: {sum(quantidade_de_sacos_semana)} sacos")
print(f"\nDias em que o consumo foi acima de 29 sacos:")
print(*quantidade_de_sacos_limite)



                



