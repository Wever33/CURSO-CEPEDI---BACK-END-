nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))

media = (nota_1+nota_2)/2

if media > 6:
    print(f"Aluno aprovado! Média = {media}")
else:
    print(f"Aluno reprovado! Média = {media}")