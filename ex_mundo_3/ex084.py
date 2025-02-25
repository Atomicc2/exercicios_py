#Lê varios nomes e pessoas e retorna alguns parêmtros

dados = []
pessoas = []
pesado = 0
leve = 0

while True:

    dados.append(str(input("Nome: ")))
    dados.append(int(input("peso: ")))
    pessoas.append(dados[:])
    
    if len(pessoas) == 1:
        pesado = dados[1]
        leve = dados[1]
    if dados[1] > pesado:
        pesado = dados[1]
    if dados[1] < leve:
        leve = dados[1]

    dados.clear()

    resp = str(input("Quer continuar? [S/N] "))
    if resp in 'Nn':
        break

pessoas_pesadas = []
pessoas_leves = []

for pessoa in pessoas:
    if pessoa[1] == pesado:
        pessoas_pesadas.append(pessoa[0])
    if pessoa[1] == leve:
        pessoas_leves.append(pessoa[0])

print(f"Você cadastrou um total de {len(pessoas)} pessoas!")
print(f"A(s) pessoa(s) mais pesada(s) é/são: {pessoas_pesadas}")       
print(f"A(s) pessoa(s) mais leve(s) é/são: {pessoas_leves}")