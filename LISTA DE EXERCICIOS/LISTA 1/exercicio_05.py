salario_mensal = float(input("Sálario Mensal: "))
porcentual_reajuste = float(input("Porcentual de reajuste (%): "))

salario_novo = salario_mensal
salario_novo += (salario_mensal*porcentual_reajuste)/100


print(f"Sálario antigo: {salario_mensal}\nReajuste: {porcentual_reajuste}%\nNovo sálario: {salario_novo}")