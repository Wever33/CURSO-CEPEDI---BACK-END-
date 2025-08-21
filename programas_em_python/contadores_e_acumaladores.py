contador_par = 0
soma_impar = 0
for i in range(1,121):
    if i%2 == 0:
        contador_par += 1
    else:
        soma_impar += i
print(f"No intervalo [1,120] existem {contador_par} números pares ")        
print(f"No intervalo [1,120] somamos {soma_impar} em números ímpares ")        