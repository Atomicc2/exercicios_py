#gera número número aleátórios e seleciona-os da tuplam e mostra qual o maior e o menor

from random import randint


numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in range(0, 5):
    random = randint(0, 10)
    print(f"{numbers[random]}", end=' ')
    if i == 0:
        menor = numbers[random]
        maior = numbers[random]
    if numbers[random] < menor:
        menor = numbers[random]
    elif numbers[random] > maior:
        maior = numbers[random]


print(f"\nO maior número é {maior} e o menor é {menor}")