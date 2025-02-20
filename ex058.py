#refasendo o desafio 28 

import random
from time import sleep

random_number = random.randint(0, 10)

number = int(input("I generate a random number between 1 and 10, try to guess! "))

tentativas = 0
while random_number != number:
    number = int(input("Bad, try again: "))
    tentativas += 1

print(f"Yes, congratulations, you got it right in {tentativas} attempts!")