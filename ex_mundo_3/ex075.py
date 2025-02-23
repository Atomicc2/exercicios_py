#Requisitando 4 valores e adionando em uma tupla s depois mostrando alguns dados 

num = tuple(int(input("Digite um número: ")) for i in range(0, 4))

num_9 = num.count(9)

if num_9 > 1:
    print(f"O valor 9 apareceu {num_9} vezes!")
elif num_9 == 1:
    print("O valor 9 aparçeu 1 vez!")
else:
    print("O valor 9 não apareceu nenhuma vez!")

if num.count(3) > 0:
    print(f"O valor 3 apareceu na posição {(num.index(3) + 1)}")
else:
    print("Não teve nenhuma valor 3!")

par = 0
for i in range(0, len(num)):
    if (num[i] % 2) == 0:
        par += 1

if par > 1:
    print(f"Você digitou {par} números pares!")
elif par == 1:
    print("Você digitou 1 número par!")
else: 
    print("Você não digitou números pares!")