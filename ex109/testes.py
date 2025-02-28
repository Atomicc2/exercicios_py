#Criando um múdulo com algumas funções

import moeda

n = int(input("Digite um número: "))

print(moeda.aumentar_10(n, format=True))
print(moeda.diminuir_10(n, format=True))
print(moeda.dobro(n, format=True))
print(moeda.metade(n, format=(True)))
