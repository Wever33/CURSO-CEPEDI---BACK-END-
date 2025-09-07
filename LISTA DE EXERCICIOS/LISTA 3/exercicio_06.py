numero_de_funcionarios = int(input("Quantidade de funcionários: "))
nome = ""
salario = 0
departamento = ""
dicionario_funcionario = {}
maior_salario = 0
soma_salario = 0
contador_departamento = 0
lista_salario = []
nomes_departamento = ""

for i in range(numero_de_funcionarios):
    
    nome = input("Nome: ")
    salario = float(input("Salário: "))
    lista_salario.append(salario)
    departamento = input("Departamento (Vendas, RH ou Gerência): ").upper()
    print("-------------------------------------------------------")
    dicionario_funcionario [nome] = [salario, departamento]

maior_salario = max(lista_salario)

for nome, (salario, departamento) in dicionario_funcionario.items():

    if departamento == "VENDAS":
        contador_departamento += 1
        nomes_departamento += f"{nome}, "

    if salario == maior_salario:
        print(f"\n ● O funcionário(a) que contém o maior salário: {nome} R$ ({salario:.2f}) ")

    


print(f" ● A quantidade de funcionários que trabalham no departamento de Vendas: {contador_departamento} ({nomes_departamento})")
print(f" ● A média dos salários dos funcionários: R$ {sum(lista_salario) / len(lista_salario):.2f} ")
