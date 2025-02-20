#Retornando a menor e a maior idade
maior = 0
menor = 0
for i in range(1, 6):
    idade = int(input("Me fale as idades: "))
    if idade > maior:
        maior = idade
    elif idade < menor:
        menor = idade
    else:
        menor = idade
print(f"A maior idade é {maior} e a menor é {menor}")