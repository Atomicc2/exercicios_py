#Lê o nome e o total de partidas de um jogador, depois pergunta a quantidae de gols em cada uma e retorna alguns parâmetros

data = {}

data['nome'] = str(input("Me fale o nome do jogador: "))
data['jogos'] = int(input("Quantos jogos? "))
gols = []
tot = 0
for i in range(1, data['jogos'] + 1):
    gols.append(int(input(f"Quantos gols no {i}º jogo? ")))

data['gols'] = gols
data['total'] = sum(gols)

print('===' * 20)
print(f"{data}")
print('===' * 20)

for i, j in data.items():
    print(f"A key {i} tem o value {j}")

print('===' * 20)
print(f"O jogador {data['nome']} jogou {data['jogos']} jogos")

for i in range(1, data['jogos']): 
    print(f"{'=>':>5} No jogo {i} ele fez {data['gols'][i - 1]}")