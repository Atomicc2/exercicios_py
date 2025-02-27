#4 jogadores jogam um dado cada e diz quem ganhou

import random, time, operator

jogo = {}

for i in range(1, 5):
    jogadores = f'{i}º jogador'
    jogo[jogadores] = random.randint(1, 6)

for jogador, numero in jogo.items():
    print(f"O {jogador} tirou {numero} no dado")

ranking = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)

for posi, j  in enumerate(ranking):
    print(f"O {j[0]} ficou na {posi + 1}º posição com o número {j[1]} sorteado")






