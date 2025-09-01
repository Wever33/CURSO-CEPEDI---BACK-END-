mensagem_menu = """

----------------- TABELA IDADE -----------------
[IDADE ATÉ 12] = CRIANÇA
[IDADE 13 ATÉ 17] = ADOLESCENTE
[IDADE MAIOR QUE 18] = ADULTO 
------------------------------------------------
"""

print(mensagem_menu)
quantidade_de_pessoas = int(input("Quantidade de pessoas para verificação: "))


for i in range(quantidade_de_pessoas):

    idade = int(input("Idade: "))

    if idade >= 0 and idade <= 12:
        print("Categoria: Criança\n")

    elif idade >= 13 and idade <= 17:
        print("Categoria: Adolescente\n") 

    else:
        print("Categoria: Adulto\n") 
