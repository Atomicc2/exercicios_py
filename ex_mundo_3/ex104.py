#Função que lê um número e dar erro caso n seja um  número inteiro

def num(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print("ERRO, Digite um  número inteiro")
    return valor

n = num("Digite um número: ")
print(f"Você digitou o número {n}")