altura = 0 
sexo = 0
#lista_altura_masculino = []
lista_altura_feminino = []
lista_altura_sala = []
contador = 0

print(" [1] - Masculino\n [2] - Feminino")

while True:

    sexo = int(input("\nOpção sexo: "))

    if sexo == 1:

        altura = float(input("\nDigite a altura (m): "))
        #lista_altura_masculino.append(altura)
        lista_altura_sala.append(altura)
        contador += 1

    elif sexo == 2:
        
        altura = float(input("\nDigite a altura (m): "))
        lista_altura_feminino.append(altura)
        lista_altura_sala.append(altura)
        contador += 1

    else:
        print("Digite uma opção válida, 1 ou 2")

    if contador == 50:
        break

print("\n-------------------------------------------------------------------------------------------------------------")
print(f"\n A maior altura da turma: {max(lista_altura_sala):.2f} m\n A menor altura da turma: {min(lista_altura_sala):.2f} m")
print(f"\n Média da altura das mulheres: {sum(lista_altura_feminino) / len(lista_altura_feminino):.2f} m")
print(f"\n Média da altura da turma: {sum(lista_altura_sala) / len(lista_altura_sala):.2f} m")
print("\n-------------------------------------------------------------------------------------------------------------")
    
