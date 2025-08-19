taxa = float(input("Taxa: "))
capital = float(input("Capital: "))
tempo = float(input("Tempo: "))

juros_simples = (capital*taxa*tempo)/100
juros_composto = capital*(1+taxa)**tempo

print("Juros simples = ", juros_simples)
print("Juros compostos = ", juros_composto)