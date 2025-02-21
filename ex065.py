#Lê vário número, diz a média o maior e o menor 

print("Digite a quantidade de números que desejar e eu te direi a média entre eles e qual foi maior e o menor!")

resposta = "S"
maior = 0
menor = 0
soma = 0
total = 0

while resposta in "S":
    
    total += 1
    num = int(input("Digite os números aqui: "))
    if total == 1:
         menor = maior = num
    if  num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    resposta = str(input("Deseja continuar? [S/N]")).upper()

media = soma / total

print(f"A média dos valores é {media:.1f}, o maior é {maior} e o menor é {menor}!")
    
    