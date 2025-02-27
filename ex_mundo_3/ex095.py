#Aprimorando o software do ex 93

time = []
jogador = {}
gols = []

while True:
    
    jogador['nome'] = str(input("Nome: ")) 
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    
    for i in range(1, partidas + 1):
        gols.append(int(input(f"Quantos gols na {i}ª partida? ")))
    
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

print("-" * 39)
print(f"cod", end=' ')
for i in jogador.keys():
    print(f"{i:<15}", end='')
print()
print("-" * 39)
for i, j in enumerate(time):
    print(f"{i + 1:>3}", end=' ')
    for k in j.values():
        print(f"{str(k):<15}", end='')
    print()
print("-" * 39)

while True:
    busca = int(input("De qual jogador quer ver os dados? (999 encerra) "))
    if busca == 999:
        break
    elif busca > len(time):
        print("ERRO! Jogador não encontrado, digite um número válido!")
    else:
        busca -= 1
        print(f"---LEVANTAMENTO DO JOGADOR {time[busca]['nome']}---")
        for i, j in enumerate(time[busca]['gols']):
            print(f"No jogo {i + 1} ele fez {j} gols!") 
        