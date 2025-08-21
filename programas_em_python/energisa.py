mensagem = """


  PREÇO POR TIPO E FAIXA DE CONSUMO:

============|==============|==========|
    TIPO    | FAIXA (KWH)  | PREÇO    |
============|==============|==========|
            |              |          |
RESIDENCIAL | ATÉ 500      | R$ 0,40  |
            | ACIMA DE 1000| R$ 0,65  |
------------|--------------|----------|            
            |              |          |
COMERCIAL   | ATÉ 1000     | R$ 0,55  |
            | ACIMA DE 1000| R$ 0,60  |
------------|--------------|----------|
            |              |          |
INDUSTRIAL  | ATÉ 5000     | R$ 0,55  |
            | ACIMA DE 5000| R$ 0,60  |
------------|--------------|----------|

---------- TIPO DE INSTALAÇÃO ----------

[I] - INSDÚSTRIA
[C] - COMÉRCIO
[R] - RESIDÊNCIA

----------------------------------------
"""
tipo_de_instalacao = input(mensagem).upper()
valor_a_pagar = 0


if tipo_de_instalacao == "R":

    energia_consumida = float(input("Energia consumida (em KWH): "))

    if energia_consumida <= 500:
        valor_a_pagar = energia_consumida*0.40
        print(f"Valor a pagar: {valor_a_pagar:.2f}")
    else:
        valor_a_pagar = energia_consumida*0.65
        print(f"Valor a pagar: {valor_a_pagar:.2f}")

elif tipo_de_instalacao == "I":

    energia_consumida = float(input("Energia consumida (em KWH): "))

    if energia_consumida <= 5000:
        valor_a_pagar = energia_consumida*0.55
        print(f"Valor a pagar: {valor_a_pagar:.2f}")

    else: 
        valor_a_pagar = energia_consumida*0.60
        print(f"Valor a pagar: {valor_a_pagar:.2f}")

elif tipo_de_instalacao == "C":

    energia_consumida = float(input("Energia consumida (em KWH): "))

    if energia_consumida <= 1000:
        valor_a_pagar = energia_consumida*0.55
        print(f"Valor a pagar: {valor_a_pagar:.2f}")

    else:
        valor_a_pagar = energia_consumida*0.60
        print(f"Valor a pagar: {valor_a_pagar:.2f}")

else:
    print("Tipo de instalação invalida!")