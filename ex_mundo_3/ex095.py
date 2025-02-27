#Aprimorando o software do ex 93

time = []
jogador = {}
gols = []

while True:
    
    jogador['nome'] = str(input("Nome: ")) 
    jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    
    for i in range(1, jogador['partidas'] + 1):
        gols.append(int(input(f"Quantos gols na {i}ª partida?")))
    
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()

    while True:
        resposta = str(input("Deseja adicionar mais algum jogador ao time? [S/N] ")).upper()
        if resposta not in 'SN':
            print("ERRO! Digite apenas S ou N!")
        else:
            break
    if resposta in 'N':
        break
print("---" * 20)

