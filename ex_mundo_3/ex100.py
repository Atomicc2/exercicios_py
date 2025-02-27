#Função que ger números e soma apenas os pares

import random, time


def gerador(lista):
    print("Sorteando 5 valores: ")
    while len(lista) < 5:
        num = random.randint(0, 9)
        lista.append(num)
        print(num, end=' ', flush=True)
        time.sleep(0.3)
    print()

def soma_pares(lista):
    total = 0
    for i in lista:
        if i % 2 == 0:
            total += i
    print(f"O total dos pares somados é {total}")

numeros = []
gerador(numeros)
soma_pares(numeros)