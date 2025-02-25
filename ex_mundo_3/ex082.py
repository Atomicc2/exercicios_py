#Criando uma lista, depois criando mais 2 com apenas os números pares e outra com os números ímpares
valores = []
valores_par = []
valores_impar = []

while True:
    n = int(input("Digite um número: "))
    valores.append(n)
    if n % 2 == 0:
        valores_par.append(n)
    else:
        valores_impar.append(n)
    resposta = str(input("Quer adicionar mais? [S/N]")).upper()
    if resposta in 'N':
        break

print(f"Você digitou os valores {valores}")
print(f"Os pares são {valores_par}")
print(f"Os ímpares são {valores_impar}")
