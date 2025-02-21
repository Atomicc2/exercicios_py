#Jogo jokempô contra o compuador

from random import randint
from time import sleep

#Definindo a resposta do random
numero = randint(1, 3)

if numero == 1:
    computador = "Pedra"
elif numero == 2:
    computador = "Papel"
elif numero == 3:
    computador = "Tesoura"

print("Vamos jogar jokenpô?")
print("Você escolhe: ")
player = int(input("1 - Pedra\n2 - Papel\n3- Tesoura\n"))

if player == 1:
    voce = "Pedra"
elif player == 2:
    voce = "Papel"
elif player == 3:
    voce = "Tesoura"

if 1 <= player <= 3:
    print("Muito bem, vamos ver o resultado!")
else:
    print("Essa não é uma opção válida!")

print("\033[1m-=-\033[m" * 10)
if player == numero:
    print("Draw!")
elif (player == 1 and numero == 3) or (player == 2 and numero == 1) or (player == 3 and numero == 2):
    print("Você ganhou!")
    print(f"Você jogou {voce}")
    print(f"Computador jogou {computador}")
else:
    print("Você perdeu!")
    print(f"Você jogou {voce}")
    print(f"Computador jogou {computador}")
print("\033[1m-=-\033[m" * 10)



