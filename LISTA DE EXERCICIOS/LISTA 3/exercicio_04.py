PALAVRA_SECRETA = "Programação"
texto = ""

while True:
        
        texto = input("Texto aqui: ").title()

        if texto == PALAVRA_SECRETA:
                print(f"\nParanbés você acertou a palavra secreta => '{PALAVRA_SECRETA}'\n")
                break
        else:
            print(f"'{texto}' não é a palavra secreta. Tente novamente! \n")
