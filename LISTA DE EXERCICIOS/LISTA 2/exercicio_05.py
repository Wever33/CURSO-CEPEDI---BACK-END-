idade = int(input("Idade: "))
tempo_de_servico = int(input("Tempo de serviço: "))

if idade >= 65 or tempo_de_servico >= 30 or (idade >= 60 and tempo_de_servico >= 25):
    print("Você pode se aposentar")
else:
    print("Você não pode se aposentar")
