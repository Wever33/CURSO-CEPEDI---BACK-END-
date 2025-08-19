mensagem_boas_vindas = """
-------------------- BEM VINDO A NOSSA LOJA -------------------
OPÇÕES PARA SEGUIR:

        1 => [A VISTA - COM DESCONTO DE 15% - APROVEITE!]
        2 => [CARTÃO]

-------------------- OPÇÕES ADICIONAIS ------------------------

        3 => [SAIR DA LOJA]
        4 => [NOTA FISCAL]

---------------------------------------------------------------
"""
print(mensagem_boas_vindas)

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))

opcao = int(input("Escolha umas das opções: "))

A_VISTA = 1
CARTAO = 2
if opcao == A_VISTA:
    desconto = preco*0.15
    preco_a_pagar = preco - desconto
    print(f"Valor a pagar {preco_a_pagar}")
        




