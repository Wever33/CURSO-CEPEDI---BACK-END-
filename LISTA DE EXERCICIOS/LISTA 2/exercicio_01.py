mensagem_menu = """


-------------------- BEM VINDO(A) --------------------

CUPONS DISPONÍVEIS EM NOSSA LOJA:    

●  CÓDIGO - [desconto10]: Desconto de 10%

●  CÓDIGO - [fretegratis]: R$ 15,00 off sobre o valor.

------------------------------------------------------


"""

LIMITE_DE_CUPONS = 2
valor_final_compra = 0
contador = 0
 

print(mensagem_menu)
valor_total_compra = float(input("VALOR TOTAL DA COMPRA (R$): "))

if valor_total_compra > 0:

    while contador < 2:

        if LIMITE_DE_CUPONS <= 2:
            cupom_de_desconto = input("DIGITE O CÓDIGO DO CUPOM: ").lower()

            if cupom_de_desconto == "desconto10":
                contador += 1
                print("CUPOM 'desconto10' APLICADO ")
                valor_final_compra = valor_total_compra - (valor_total_compra*0.1)

            elif cupom_de_desconto == "fretegratis":
                contador += 1
                print("CUPOM 'fretegratis' APLICADO")
                valor_final_compra -= 15
            
            else:
                print("CUPOM INVÁLIDO, TENTE NOVAMENTE!")
    else:
        mensagem_extrato = f"""
-------------------- NOTA FISCAL --------------------

VALOR SEM DESCONTO: R$ {valor_total_compra:.2f}

CUPOM [desconto10]: 10% OFF - APLICADO
CUPOM [fretegratis]: R$ 15 OFF - APLICADO

VALOR COM DESCONTO: R$ {valor_final_compra:.2f}

-----------------------------------------------------
"""
        print(mensagem_extrato)

else:
    print("Digite valores positivos, por favor ")         
    

                        


