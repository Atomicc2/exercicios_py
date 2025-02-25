#Lê valores digitados e diz qual a posição do maior e dor menor

valores = []

for i in range(0, 5):
    valores.append(input("Digite os números: "))

maior = max(valores)
menor = min(valores)

for p, i in enumerate(valores):
    if i == maior:
        posição_maior = p
    if i == menor:
        posição_menor = p

print(f"O maior valor ({maior}) está na posição {posição_maior + 1}")
print(f"O menor valor ({menor}) está na posição {posição_menor + 1}")
