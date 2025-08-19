nome_aluno = input("Digite seu nome: ")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))



media = (nota1+nota2)/2

if media > 6:
    mensagem_situacao = "Aprovado"
else:
    mensagem_situacao = "Reprovado"


mensagem = f"""
 -------------Área do Aluno------------
 Aluno: {nome_aluno}
 Notas: {nota1} | {nota2}
 Média: {media}
 Situação: {mensagem_situacao} 
"""

print(mensagem)