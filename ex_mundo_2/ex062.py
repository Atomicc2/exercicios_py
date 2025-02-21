#refafazendo o 61 porém adicionando uma condição a mais para seguir

p1 = int(input("Me fale o primeiro termo da PA: "))
razao = int(input("Me fale a razão da PA: "))
termo = 10

print("Os 10 primeiros termos são: ")
while termo != -1:
    if termo > 0:
        print(p1, end=' - ')
    termo -= 1
    p1 += razao
    if termo == 0:
        termo = int(input("Quer adiconar mais quantos termos? "))
    