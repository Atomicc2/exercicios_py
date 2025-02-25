#lê varios valores e retorna eles em ordem crescente

valores = []

while True:

    numero = int(input("Digite o valor: "))
    if numero in valores:
        print(f"O valor {numero} já foi adicionado!")
    else:
        valores.append(numero)

    resposta = ''
    resposta = input("Deseja continuar? [S/N] ").upper()
    if resposta in 'N':
        break

valores.sort()
print(f"Você digitou os valores {valores}")