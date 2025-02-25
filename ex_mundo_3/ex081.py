#Lê vários números e mostra alguns parâmetros

valores = []
contagem = 0
numero_5 = 'N'

while True:
    n = (int(input("Digite um número: ")))
    valores.append(n)
    resposta = str(input("Mais algum? [S/N] "))
    contagem += 1
    if n == 5:
        numero_5 = 's'

    if resposta in 'Nn':
        break

valores.sort(reverse=True)

print(f"Você digitou {contagem} números")
print(f"Os números digitados (em ordem decrescente): {valores}")
if numero_5 in 's':
    print("Você digitou o número 5")
else:
    print("Você não digitou o número 5")