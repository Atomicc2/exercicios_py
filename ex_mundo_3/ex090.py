#Lê o nome e média de um aluno e retorna a sua situação

alunos = []
informacoes_aluno = {}

informacoes_aluno['nome'] = str(input("Nome: "))
informacoes_aluno['media'] = float(input(f"Média de {informacoes_aluno['nome']}: "))

print(f"O nome do aluno é {informacoes_aluno['nome']}")
print(f"Sua média é {informacoes_aluno['media']}")
if informacoes_aluno['media'] >= 6:
    print("Aluno aprovado!!!")
else:
    print("Aluno reprovado!!")
    