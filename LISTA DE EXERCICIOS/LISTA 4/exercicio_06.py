gabarito = ["a", "b", "c", "d"]
NUMERO_DE_ALUNOS = 2
matricula_aluno = 0
reposta = ""
NUMERO_DE_QUESTOES = len(gabarito)
lista_de_matriculas = []
boletim_geral = []
mensagem_aluno = ""
situacao_aluno = ""
contador_aprovados = 0

for i in range(NUMERO_DE_ALUNOS):

    matricula_aluno = int(input("Matrícula: "))
    lista_de_matriculas.append(matricula_aluno)


for matricula in lista_de_matriculas:

    print(f"Aluno de matrícula {matricula}. Responda as {NUMERO_DE_QUESTOES} questões")

    respostas_certas = 0

    for indice, reposta_gabarito in enumerate(gabarito):

        reposta = input("Reposta: ")

        if reposta == reposta_gabarito:
        
            print("Reposta certa!")
            respostas_certas += 1
            
        else:
            print(f"Resposta errada! Reposta correta {reposta_gabarito}")

    nota = (respostas_certas/NUMERO_DE_QUESTOES) * 10
    boletim_geral.append((matricula, respostas_certas, nota))
    
    if nota >= 6:
        situacao_aluno = "APROVADO"
        contador_aprovados += 1
    else:
        situacao_aluno = "REPROVADO"

    mensagem_aluno += f"""

    MATRÍCULA: {matricula}
    TOTAL DE ACERTOS: {respostas_certas}/{NUMERO_DE_QUESTOES}
    NOTA: {nota:.0f}
    SITUAÇÃO: {situacao_aluno}

    """

print(mensagem_aluno)
print(f"Porcentagem aprovados: {(contador_aprovados*100) / len(lista_de_matriculas):.0f} %")