#refasendo o desafio 28 

import random

random_number = random.randint(0, 10)

number = int(input("I generate a random number between 1 and 10, try to guess! "))

tentativas = 0
acertou = False

while not acertou:
    if number == random_number:
        acertou = True
    else:
        if number < random_number:
            number = int(input("É mais... Tente denovo: "))
        else:
            number = int(input("É menos... Tente denovo: "))
    tentativas += 1

print(f"Yes, congratulations, you got it right in {tentativas} attempts!")