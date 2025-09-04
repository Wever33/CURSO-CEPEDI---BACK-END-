calculo_imc = 0

print("---------- IMC ----------")
altura = float(input("Altura: "))
peso = float(input("Peso: "))
print("-------------------------")

calculo_imc = (peso/altura**2)

if calculo_imc < 18.5:
    print(f"Abaixo do peso\nIMC: {calculo_imc:.2f}")
    
elif calculo_imc >= 18.5 and calculo_imc <= 24.9:
    print(f"Peso ideal\nIMC: {calculo_imc:.2f}")
    
elif calculo_imc >= 25.0 and calculo_imc <= 29.9:
    print(f"Levemente acima do peso\nIMC: {calculo_imc:.2f}")
    
elif calculo_imc >= 30.0 and calculo_imc <= 34.9:
    print(f"Obesidade grau I\nIMC: {calculo_imc:.2f}")
    
elif calculo_imc >= 35 and calculo_imc <= 39.9:
    print(f"Obesidade grau II (severa)\nIMC: {calculo_imc:.2f}") 

else:
    print(f"Obesidade grau III (mórbida)\nIMC: {calculo_imc:.2f}")
