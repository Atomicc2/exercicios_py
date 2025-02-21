#refazendo o desafio 51, resolvendo uma PA usando usando while

p1 = int(input("Me fale o primeiro termo da PA: "))
razão = int(input("Me fame a razão da PA: "))
termo = 0

print("Os 10 primeiros termos são: ")
while termo != 10:
    print(p1, end=' - ')
    p1 += razão
    termo += 1
    