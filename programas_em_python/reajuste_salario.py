salario = float(input("Digite seu salário: "))

if salario <= 300: 
    aumento = salario*0.35
    print(f"Salário atualizado: {salario+aumento}")
elif salario > 300:
    aumento = salario*0.15
    print(f"Salário atualizado: {salario+aumento}")
else:
    print("Opss.")