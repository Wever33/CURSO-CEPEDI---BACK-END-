lista_elementos = []
numeros = 0
maior_numero = 0
menor_numero = 0
posicao_maior = 0
posicao_menor = 0

for i in range(4):
    numeros = int(input("Digite números aqui: "))
    lista_elementos.append(numeros) 

maior_numero = max(lista_elementos)
menor_numero = min(lista_elementos)

posicao_maior = lista_elementos.index(maior_numero)
posicao_menor = lista_elementos.index(menor_numero)

print("\n----------------RESULTADO---------------")
print(f"\n Maior número: {maior_numero} | Posição: {posicao_maior+1}")    
print(f" Menor número: {menor_numero} | Posição: {posicao_menor+1}")    
print("\n----------------------------------------")