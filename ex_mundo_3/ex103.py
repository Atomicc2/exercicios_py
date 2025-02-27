#Função que lê dados e tem validação

def jogador(nome='<desconhecido>', gols=0):

    print(f"O jogador {nome} fez {gols} gols!!")

n = str(input("Nome: "))
g = str(input("Gols: "))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    jogador(gols=g)
else:
    jogador(nome=n, gols=g)

