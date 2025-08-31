senha = 0
dicionarios_usuarios = {}
usuario = ""

menu_principal = """
--------------- MENU PRINCIPAL --------------

OPÇÃO [1] - FAZER LOGIN
OPÇÃO [2] - FAZER CADASTRO
OPÇÂO [3] - SAIR

"""


while True:
    opcao = int(input(menu_principal))

    if opcao == 1:
        print("-------------------- LOGIN ------------------\n")
        usuario = input("Digite seu usuário: ") 
        senha = int(input("Digite sua senha: "))

        if usuario in dicionarios_usuarios and dicionarios_usuarios[usuario] == senha:
            print("Login feito com sucesso!")
        
        else:
            print("Falha ao fazer login. Tente novamente!")

    elif opcao == 2:

        print("-------------------- CADASTRO ------------------\n")
        usuario = input("Digite seu usuário: ")
        senha = int(input("Digite sua senha: "))

        if usuario in dicionarios_usuarios:
            print("Usuário existente, tente outro!")

        else:

            print("Conta criada com sucesso!")
            dicionarios_usuarios[usuario] = senha
    
    elif opcao == 3:
        print("Saindo do sistema..")
        break

    else:
        print("Opção Inválida")
