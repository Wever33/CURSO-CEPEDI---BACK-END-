menu = """
 Qual desses elementos queres descobrir a área:

 [1] --> Triângulo 
 [2] --> Retãngulo
 [3] --> Trapezio

"""
opcao = int(input(menu))

if opcao == 1:
    base = float(input("Base: "))
    altura = float(input("Altura:"))
    calculo_area_triangulo = (base*altura)/2
    print(f"Área do trângulo: {calculo_area_triangulo}")
elif opcao ==2:
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    calculo_area_retangulo = base*altura
    print(f"Área do retãngulo ")

elif opcao == 3:
    base_menor = float(input("Base menor: "))
    base_maior = float(input("Base maior: "))
    altura = float(input("Altura: "))
    calculo_area_trapezio = ((base_maior + base_menor)*altura)/2
    print(f"Área do trapezio: {calculo_area_trapezio}")








