#Fazeno um leitor de compras e seus preços e retornando o valor total e algumas outras coisas

total = contagem_preco = menor = contagem = 0

while True:
    
    produto = str(input("Me fale o nome do produto: "))
    preco = int(input("Me fale o preço: "))
    resposta = ' '
    total += preco
    contagem += 1

    if preco >= 1000:
        contagem_preco += 1
    if contagem == 1:
        menor = preco
    
    elif preco < menor:
        menor = preco

    while resposta not in 'SN':
        resposta = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resposta in 'N':
        break

print('-' * 15)
print(f'''O valor total é R${total}
{contagem_preco} é/são acima de R$1000
{menor} é o preço do produto mais barato!''')
print('-' * 15)