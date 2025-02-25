#Algumas anotações sobre os dicionários

pessoas = {
    'nome':'Anderson',
    'idade': 21,
    'sexo': 'Precisando'
}

print(pessoas.values())                         #Escreve os valores do dicionário
print(pessoas.keys())                           #Escreve as chaves dos valores 
print(pessoas.items())                          #Escreve tanto um como outro

cardapio = []
comidas = {}

comidas['nome'] = str(input("Qual o nome da comida? ")) 
comidas['preco'] = float(input("Qual o seu preço? "))

cardapio.append(comidas.copy())                 #Copia os valores do dicionário pra dentro da lista

print(comidas)

