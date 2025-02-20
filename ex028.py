import random
from time import sleep

random_number = random.randint(0, 5)

number = int(input("I generate a random number, try to guess! "))

print("PROCESSANDO.")
sleep(1)
print("PROCESSANDO..")
sleep(1)
print("PROCESSANDO...")
sleep(1.5)

if random_number == number:
    print("Yes, congratulations, you got it right!!")
else:
    print(f"Sad, the number was {random_number}")