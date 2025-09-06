soma = 0
media = 0
contador_pares = 0

for i in range(39,71):
    
    if i % 2 == 0:
        soma += i
        contador_pares += 1

media = soma/contador_pares

print(f"Soma dos pares entre 40 e 70: {soma}")
print(f"Média aritmética dos pares: {media}")
