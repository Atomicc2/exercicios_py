#Criando um múdulo com algumas funções

import moeda

preco = float(input("Digite o valor: "))
aumento = float(input("Porcentagem de aumento: "))
diminuicao = float(input("Porcentagem de diminuição: "))

print(moeda.resumo(preco, aumento, diminuicao))