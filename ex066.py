#Lê varios números retorna a soma e a quantidade de números digitados

soma = 0
num = 0
contador = 0

print("A condição de parada é digitar [ 999 ]")

while True:
    num = int(input("Me diga um número: "))
    if num == 999:
        break
    soma += num
    contador += 1

print(f"Você digitou {contador} números e a soma deles é {soma}")