#Fazendouma taboada infinita com a condição de digitar um número negativo para parar

num = 0
contador = 0

while True:
    num = int(input("Digite o número ao qual deseja ver a taboada:\n"))
    if num < 0:
        break
    print("-=-" * 6)
    for contador in range(1, 11):
        print(f"{num} X {contador} = {num * contador}")
    print("-=-" * 6)