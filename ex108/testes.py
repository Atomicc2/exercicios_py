#Criando um múdulo com algumas funções

import moeda

n = int(input("Digite um número: "))

print(moeda.moeda(moeda.aumentar_10(n)))
print(moeda.moeda(moeda.diminuir_10(n)))
print(moeda.moeda(moeda.dobro(n)))
print(moeda.moeda(moeda.metade(n)))
