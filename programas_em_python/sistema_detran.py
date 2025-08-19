from datetime import datetime

velocidade_carro = int(input("Velocidade carro (Km/h): "))
VELOCIDADE_MAXIMA = 80
multa = 0
velocidade_ultrapassada = 0
data_multa = datetime.now()
mascara_data = "%d/%m/%Y"
mascara_horario = "%H:%M"

if velocidade_carro > 80:
    velocidade_ultrapassada = velocidade_carro - 80
    multa = velocidade_ultrapassada*15

    mensagem_multa = f"""
    -------------------------------------------
        MULTA POR EXCESSO DE VELOCIDADE

    VALOR DA MULTA: R$ {multa:.2f}
    VELOCIDADE: {velocidade_carro} KM/H
    LIMITE DA VIA: 80 KM/H
    INFRAÇÃO: MÉDIA
    DATA DA INFRAÇÃO: {data_multa.strftime(mascara_data)}
    HORÁRIO DA INFRAÇÃO: {data_multa.strftime(mascara_horario)}
    -------------------------------------------
    """
    print(mensagem_multa)
else:
    print("O senhor não levou multa!")