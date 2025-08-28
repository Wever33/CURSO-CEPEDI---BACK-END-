
total_eleitores = int(input("Número total de eleitores: "))
total_votos_brancos = int(input("Votos brancos: "))
total_votos_nulos = int(input("Votos nulos: "))
total_votos_validos = int(input("Votos válidos: "))
soma_votos = total_votos_brancos+total_votos_nulos+total_votos_validos

if soma_votos < total_eleitores:
    print("Ocorreu um erro na contagem de votos, Tente novamente!")
else:
    print(f"Porcentual de votos brancos: {((100*total_votos_brancos)/total_eleitores):.2f} %")
    print(f"Porcentual de votos nulos: {((100*total_votos_nulos)/total_eleitores):.2f} %")
    print(f"Porcentual de votos válidos: {((100*total_votos_validos)/total_eleitores):.2f} %")